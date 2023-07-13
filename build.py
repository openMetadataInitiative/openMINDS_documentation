import os.path
import shutil

from pipeline.schema import SchemaDocBuilder
from pipeline.instance import InstancesLibraryBuilder, InstancesDocBuilder
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

##################################
# A: gather schema specifications
##################################

# Step 1 - clone central repository in main branch to get the latest sources
schema_loader = SchemaLoader()

for schema_version in schema_loader.get_schema_versions():

    # Step 2 - building static structure
    copy_static_structures(schema_version)

    # Step 3 - find all involved schemas for the current version
    schemas = schema_loader.find_schemas(schema_version)
    relative_path_by_schema = schema_loader.get_relative_path_for_schemas(schemas, schema_version)

    for schema in schemas:
        # Step 4 - build documentation for version specific schema
        SchemaDocBuilder(schema, schema_loader.schemas_sources, relative_path_by_schema).build()

    # Step 5 - building toctrees (please note that the implementation requires the schemas to be built already)
    create_toc_tree_page(schema_version, ["schema_specifications"])

    # Step 6 - checkout version branch in relative "upload" directory (provided by GitHub pipeline), copy files and push
    if schema_version not in versions:
        versions.append(schema_version)

######################
# B: gather instances
######################

# Step 1 - clone instances repository in main branch to get the latest sources
instance_loader = InstanceLoader()

for instance_version in instance_loader.get_instance_versions():
    instances_libraries = InstancesLibraryBuilder()

    # Step 2 - find all involved schemas for the current version
    instances = instance_loader.find_instances(instance_version)
    relative_path_by_instance = instance_loader.get_relative_path_for_instances(instances, instance_version)

    for instance in instances:
        # Step 3 - gather version specific instance libraries for documentation build
        instances_libraries.load_instance(instance, instance_loader.instances_sources)
        instances_libraries.add_instance_to_library()

    # Step 4 - build documentation for version specific schema
    InstancesDocBuilder(instance_version, instances_libraries.instances_libraries).build()

    # Step 5 - building toctrees (please note that the implementation requires the schemas to be built already)
    create_toc_tree_page(instance_version, ["instances_libraries"])

    # Step 6 - checkout version branch in relative "upload" directory (provided by GitHub pipeline), copy files and push
    if instance_version not in versions:
        versions.append(instance_version)

########################################################################################################################
# Step FINAL (A+B) - checkout version branch in relative "upload" directory (provided by GitHub pipeline), copy files and push
########################################################################################################################

for version in versions:
    git_pusher.upload(version)