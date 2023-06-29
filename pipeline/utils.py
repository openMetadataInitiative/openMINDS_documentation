import glob
import os
import shutil
from typing import List

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



class GitPusher(object):

    def __init__(self):
        self.upload_dir = "upload"
        self._repo = Repo(self.upload_dir)

    def upload(self, version):
        self._checkout(version)
        self._clear_directory()
        shutil.copytree(f"target/{version}", self.upload_dir, dirs_exist_ok=True)
        self._repo.git.add('--all')
        self._repo.index.commit(f'Updating documentation for version {version}')
        self._repo.git.push("origin", version)

    def _clear_directory(self):
        for item in os.listdir(self.upload_dir):
            if os.path.isdir(f"{self.upload_dir}/{item}") and not item.startswith("."):
                shutil.rmtree(f"{self.upload_dir}/{item}")
            elif os.path.isfile(f"{self.upload_dir}/{item}"):
                os.remove(f"{self.upload_dir}/{item}")

    def _checkout(self, version):
        self._repo.git.reset('--hard')
        try:
            self._repo.git.checkout(version)
        except GitCommandError as e:
            self._repo.git.checkout("-b", version)


