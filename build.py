import os.path
import shutil

from pipeline.schema import SchemaDocBuilder
from pipeline.toctree import create_toc_tree_page
from pipeline.utils import clone_sources, SchemaLoader, copy_static_structures, GitPusher

print("***************************************")
print(f"Triggering the generation of documentation for openMINDS")
print("***************************************")

# Step 1 - clone central repository in main branch to get the latest sources
clone_sources()
schema_loader = SchemaLoader()
if os.path.exists("target"):
    shutil.rmtree("target")

git_pusher = GitPusher()

for schema_version in schema_loader.get_schema_versions():

    # Step 2 - building static structure
    copy_static_structures(schema_version)

    # Step 3 - find all involved schemas for the current version
    schemas = schema_loader.find_schemas(schema_version)

    for schema in schemas:
        # Step 4 - build documentation for version specific schema
        SchemaDocBuilder(schema, schema_loader.schemas_sources).build()

    # Step 5 - building toctrees (please note that the implementation requires the schemas to be built already)
    create_toc_tree_page(schema_version, ["specifications"])

    # Step 6 - checkout version branch in relative "upload" directory (provided by GitHub pipeline), copy files and push
    git_pusher.upload(schema_version)


    # create_specifications(schema_version)