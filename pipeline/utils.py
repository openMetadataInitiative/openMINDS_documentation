import glob
import os
import shutil
from typing import List, Dict

from git import Repo, GitCommandError


def copy_static_structures(version:str):
    shutil.copytree("static", f"target/{version}")


def clone_sources():
    if os.path.exists("sources"):
        shutil.rmtree("sources")
    Repo.clone_from("https://github.com/openMetadataInitiative/openMINDS.git", to_path="sources", depth=1)


class SchemaLoader(object):

    def __init__(self):
        self._root_directory = os.path.realpath(".")
        self.schemas_sources = os.path.join(self._root_directory, "sources", "schemas")

    def get_schema_versions(self) -> List[str]:
        return os.listdir(self.schemas_sources)

    def find_schemas(self, version:str) -> List[str]:
        return glob.glob(os.path.join(self.schemas_sources, version, f'**/*.schema.omi.json'), recursive=True)

    def get_relative_path_for_schemas(self, schemas:List[str], version:str) -> Dict:
        relative_path_by_schema = {}
        for schema in schemas:
            schema_name = os.path.basename(schema).replace('.schema.omi.json', '')
            schema_name = ''.join(s[0].upper() + s[1:] for s in schema_name.split())
            relative_schema_path = os.path.relpath(schema, start=os.path.join(self.schemas_sources, version)).replace('.schema.omi.json', '')
            relative_path_by_schema[schema_name] = relative_schema_path
        return relative_path_by_schema


class GitPusher(object):

    def __init__(self):
        self.upload_dir = "../upload"
        self._repo = Repo(self.upload_dir)

    def upload(self, version):
        print(f"Uploading version {version}")
        self._checkout(version)
        self._clear_directory()
        shutil.copytree(f"target/{version}", self.upload_dir, dirs_exist_ok=True)
        self._repo.git.add('--all')
        diff_list = self._repo.head.commit.diff()
        if diff_list:
            print(f"{len(diff_list)} changes found - pushing to origin")
            self._repo.index.commit(f'Updating documentation for version {version}')
            self._repo.git.push("origin", version)
        else:
            print("No changes - nothing to commit")

    def _clear_directory(self):
        for item in os.listdir(self.upload_dir):
            if os.path.isdir(f"{self.upload_dir}/{item}") and not item.startswith("."):
                shutil.rmtree(f"{self.upload_dir}/{item}")
            elif os.path.isfile(f"{self.upload_dir}/{item}"):
                os.remove(f"{self.upload_dir}/{item}")

    def _checkout(self, version):
        self._repo.git.fetch()
        try:
            self._repo.git.checkout(version)
        except GitCommandError as e:
            self._repo.git.checkout("-b", version)


