import os.path
import shutil

from pipeline.schema import SchemaDocBuilder
from pipeline.instance import InstancesDocBuilder
from pipeline.toctree import create_toc_tree_page
from pipeline.utils import clone_sources, SchemaLoader, InstanceLoader, copy_static_structures, GitPusher

print("***************************************")
print(f"Triggering the generation of documentation for openMINDS")
print("***************************************")

# Step 0 (A+B) - clone central and instance repository (main branch) to get the latest sources
clone_sources()
if os.path.exists("target"):
    shutil.rmtree("target")

git_pusher = GitPusher()
versions = []

#####################################################
# Gather schema specifications and instance libraries
#####################################################

# Step 1 - clone central repository in main branch to get the latest sources
schema_loader = SchemaLoader()
instance_loader = InstanceLoader()

for version in schema_loader.get_schema_versions():

    # Step 2 - building static structure
    copy_static_structures(version)

    # Step 3 - find all involved schemas for the current version
    absolute_paths_for_schemas = schema_loader.find_schemas(version)
    relative_paths_for_schema_docu = schema_loader.get_relative_paths_for_schema_docu(absolute_paths_for_schemas, version)

    # Step 4 - find all involved instances for the current version
    relative_paths_for_instancelib_docu = None
    instancelib_docu_path_for_schemas = None
    if version in instance_loader.get_instance_versions():
        absolute_paths_for_instances = instance_loader.find_instances(version)
        relative_paths_for_instancelib_docu, instancelib_docu_path_for_schemas = instance_loader.get_relative_paths_and_schemas_for_instancelib_docu(absolute_paths_for_instances, version)

    # Step 5 - build documentation page for each version specific schema
    for absolute_path_schema in absolute_paths_for_schemas:
        # Step 5.1 - retrieve schema name from absolute path
        schema_name = schema_loader.get_schema_name(absolute_path_schema)
        # Step 5.2 - retrieve path to instance library path if available for schema
        if instancelib_docu_path_for_schemas and schema_name in instancelib_docu_path_for_schemas:
            instancelib_docu_path_for_schema = instancelib_docu_path_for_schemas[schema_name]
        else:
            instancelib_docu_path_for_schema = None
        # Step 5.3 - build schema documentation page
        SchemaDocBuilder(absolute_path_schema, schema_name, version, relative_paths_for_schema_docu, instancelib_docu_path_for_schema).build()

    # Step 6 - build toctrees (please note that the implementation requires the schemas to be built already)
    create_toc_tree_page(version, ["schema_specifications"])

    # Step 7 - build instance library documentation page for each version specific instance list
    if relative_paths_for_instancelib_docu:
        InstancesDocBuilder(relative_paths_for_instancelib_docu, version, instancelib_docu_path_for_schemas, relative_paths_for_schema_docu).build()

        # Step 8 - building toctrees (please note that the implementation requires the instances to be built already)
        create_toc_tree_page(version, ["instance_libraries"])

    # Step 9 - checkout version branch in relative "upload" directory (provided by GitHub pipeline), copy files and push
    if version not in versions:
        versions.append(version)


########################################################################################################################
# Step FINAL - checkout version branch in relative "upload" directory (provided by GitHub pipeline), copy files and push
########################################################################################################################

for version in versions:
    git_pusher.upload(version)
