import json
import os.path
import re
from typing import List, Optional, Dict

from rstcloth import RstCloth


class InstancesDocBuilder(object):

    def __init__(self, relative_paths_for_instancelib_docu:Dict, version:str, instancelib_docu_path_for_schemas:Dict, relative_paths_for_schema_docu:Dict):
        self.version = version
        self.relative_paths_for_instancelib_docu = relative_paths_for_instancelib_docu
        self.instancelib_docu_path_for_schemas = instancelib_docu_path_for_schemas
        self.schema_for_instancelib_docu_path = {v: k for k, v in instancelib_docu_path_for_schemas.items()}
        self.relative_paths_for_schema_docu = relative_paths_for_schema_docu
        self.readthedocs_url = "https://openminds-documentation.readthedocs.io/en/"

    def _target_file_without_extension(self, instancelib_docu_relative_path:str) -> str:
        return os.path.join(self.version, "docs", "instance_libraries", instancelib_docu_relative_path)

    def _capitalze_term(self, term:str):
        return term[0].upper() + term[1:]

    def _create_library_title(self, instancelib_docu_relative_path:str):
        instancelib_docu_relative_path_split = instancelib_docu_relative_path.split('/')
        instance_basename = instancelib_docu_relative_path_split[-1].replace('.jsonld', '')
        instance_basename_capitalized = self._capitalze_term(instance_basename)
        if len(instancelib_docu_relative_path_split) == 1:
            return f"{instance_basename_capitalized} library"
        else:
            subdir_name = instancelib_docu_relative_path_split[0]
            subdir_name_capitalized = self._capitalze_term(subdir_name)
            return f"{subdir_name_capitalized}: {instance_basename_capitalized} library"

    def _build_plurals(self, term: str) -> str:
        # build type plurals
        if term.endswith("s"):
            return f"{term}es"
        elif term.endswith("y"):
            return f"{term[:-1]}ies"
        else:
            return f"{term}s"

    def _replace_multi(self, term:str, old:List[str], new:str) -> str:
        for letter in old:
            term = term.replace(letter, new)
        return term

    def _build_single_instance_link(self, instanceReference:Dict) -> str:
        # get instance identity and create instance heading
        instance_id = instanceReference["@id"]
        instance_type = instance_id.split("/")[4]
        instance_heading = instance_id.split("/")[-1].casefold()

        # build type plurals
        instance_type_plural = self._build_plurals(instance_type)

        # create type depending link directory and page heading
        if instance_type in ["brainAtlas", "contentType", "commonCoordinateSpace", "license"]:
            link_dir = os.path.join(self.readthedocs_url, self.version, "instance_libraries")
            page_heading = instance_type_plural
        elif instance_type in ["parcellationEntity", "brainAtlasVersion", "commonCoordinateSpaceVersion"]:
            link_dir = os.path.join(self.readthedocs_url, self.version, "instance_libraries", instance_type_plural)
            page_heading = instance_heading.split("_")[0]
        elif instance_type in ["parcellationEntityVersion"]:
            link_dir = os.path.join(self.readthedocs_url, self.version, "instance_libraries", instance_type_plural)
            page_heading = "_".join(instance_heading.split("_")[:2])
        else:
            link_dir = os.path.join(self.readthedocs_url, self.version, "instance_libraries", "terminologies")
            page_heading = instance_type

        # create link and return RST hyperlink
        link = os.path.join(link_dir, f"{page_heading}.html#{self._replace_multi(instance_heading, ['_', '.'], '-')}")
        return f"`{instance_id.split('/')[-1]} <{link}>`_"

    def _build_multi_instance_links(self, instanceReferenceList:List) -> str:
        linklist = []
        for instanceReference in instanceReferenceList:
            linklist.append(self._build_single_instance_link(instanceReference))
        return ", ".join(linklist)

    def _build_instance_library_link(self, instanceReferenceList:List[Dict]) -> str:
        # this function assumes that all instances in list have the same type
        instance_example_id = instanceReferenceList[0]["@id"]
        instance_example_type = instance_example_id.split("/")[4]
        instance_type_plural = self._build_plurals(instance_example_type)
        instance_example_id_basename = instance_example_id.split("/")[-1]

        # page_heading and link depends on type
        if instance_example_type in ["brainAtlas", "contentType", "commonCoordinateSpace", "license"]:
            link_dir = os.path.join(self.readthedocs_url, self.version, "instance_libraries")
            page_heading = instance_type_plural
        elif instance_example_type in ["parcellationEntity", "brainAtlasVersion", "commonCoordinateSpaceVersion"]:
            link_dir = os.path.join(self.readthedocs_url, self.version, "instance_libraries", instance_type_plural)
            page_heading = instance_example_id_basename.split("_")[0]
        elif instance_example_type in ["parcellationEntityVersion"]:
            link_dir = os.path.join(self.readthedocs_url, self.version, "instance_libraries", instance_type_plural)
            page_heading = "_".join(instance_example_id_basename.split("_")[:2])
        else:
            link_dir = os.path.join(self.readthedocs_url, self.version, "instance_libraries", "terminologies")
            page_heading = instance_example_type

        # create link and return RST hyperlink
        link = os.path.join(link_dir, f"{page_heading}.html")

        return f"`cf. respective {instance_type_plural} <{link}>`_"

    def _build_simple_instances(self, instancelib_docu_relative_path:str, instances_absolute_paths:List[str]):
        target_file = os.path.join("target", f"{self._target_file_without_extension(instancelib_docu_relative_path)}.rst")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        schema_name = self.schema_for_instancelib_docu_path[instancelib_docu_relative_path]
        schema_path = self.relative_paths_for_schema_docu[schema_name]
        schema_link = os.path.join(self.readthedocs_url, self.version, "schema_specifications", f"{schema_path}.html")
        with open(target_file, "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            title = self._create_library_title(instancelib_docu_relative_path)
            doc.heading(f"{title}", char="#", overline=True)
            doc.newline()
            doc.content(f"Related schema specification: `{schema_name} <{schema_link}>`_")
            doc.newline()
            doc.content("------------")
            doc.newline()
            doc.content("------------")
            doc.newline()
            for instance_path in sorted(instances_absolute_paths):
                with open(instance_path, "r") as instance_f:
                    instance_data = json.load(instance_f)
                subtitle = instance_path.split("/")[-1].replace('.jsonld', '')
                doc.heading(subtitle, char="-")
                doc.newline()
                doc.directive(name="admonition", arg="metadata sheet")
                field_list_indent = 3
                doc.newline()
                for prop, value in sorted(instance_data.items()):
                    if type(value) == str:
                        doc.field(name=prop, value=str(value), indent=field_list_indent)
                    elif type(value) == List:
                        if all(isinstance(item, str) for item in value):
                            sorted_value_list = sorted(value)
                            doc.field(name=prop, value=", ".join(sorted_value_list), indent=field_list_indent)
                        if all(isinstance(item, Dict) for item in value):
                            doc.field(name=prop, value=self._build_multi_instance_links(value), indent=field_list_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <{title}_>`_")
                doc.newline()
                doc.content("------------")
                doc.newline()

    def _build_simple_sands_instances(self, instancelib_docu_relative_path:str, instances_absolute_paths:List[str]):
        target_file = os.path.join("target", f"{self._target_file_without_extension(instancelib_docu_relative_path)}.rst")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        instancelib_docu_relative_path_without_subdir = instancelib_docu_relative_path.split("/")[0]
        schema_name = self.schema_for_instancelib_docu_path[instancelib_docu_relative_path_without_subdir]
        schema_path = self.relative_paths_for_schema_docu[schema_name]
        schema_link = os.path.join(self.readthedocs_url, self.version, "schema_specifications", f"{schema_path}.html")
        with open(target_file, "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            title = self._create_library_title(instancelib_docu_relative_path)
            doc.heading(f"{title}", char="#", overline=True)
            doc.newline()
            doc.content(f"Related schema specification: `{schema_name} <{schema_link}>`_")
            doc.newline()
            doc.content("------------")
            doc.newline()
            doc.content("------------")
            doc.newline()
            for instance_path in sorted(instances_absolute_paths):
                with open(instance_path, "r") as instance_f:
                    instance_data = json.load(instance_f)
                subtitle = instance_path.split("/")[-1].replace('.jsonld', '')
                doc.heading(subtitle, char="-")
                doc.newline()
                doc.directive(name="admonition", arg="metadata sheet")
                field_list_indent = 3
                doc.newline()
                for prop, value in sorted(instance_data.items()):
                    if isinstance(value, (str, int, float)):
                        doc.field(name=prop, value=str(value), indent=field_list_indent)
                    elif isinstance(value, Dict) and "@id" in value.keys():
                        doc.field(name=prop, value=self._build_single_instance_link(value), indent=field_list_indent)
                    elif isinstance(value, List):
                        if all(isinstance(item, (str, int, float)) for item in value):
                            sorted_value_list = sorted([str(item) for item in value])
                            doc.field(name=prop, value=", ".join(sorted_value_list), indent=field_list_indent)
                        if all(isinstance(item, Dict) for item in value):
                            if prop == "hasAnnotation":
                                doc.field(name=prop, value="COMING SOON", indent=field_list_indent)
                            else:
                                doc.field(name=prop, value=self._build_multi_instance_links(value), indent=field_list_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <{title}_>`_")
                doc.newline()
                doc.content("------------")
                doc.newline()

    def _build_complex_sands_instances(self, instancelib_docu_relative_path:str, instances_absolute_paths:List[str]):
        target_file = os.path.join("target", f"{self._target_file_without_extension(instancelib_docu_relative_path)}.rst")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        instancelib_docu_relative_path_without_subdir = instancelib_docu_relative_path.split("/")[0]
        schema_name = self.schema_for_instancelib_docu_path[instancelib_docu_relative_path_without_subdir]
        schema_path = self.relative_paths_for_schema_docu[schema_name]
        schema_link = os.path.join(self.readthedocs_url, self.version, "schema_specifications", f"{schema_path}.html")
        with open(target_file, "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            title = self._create_library_title(instancelib_docu_relative_path)
            doc.heading(f"{title}", char="#", overline=True)
            doc.newline()
            doc.content(f"Related schema specification: `{schema_name} <{schema_link}>`_")
            doc.newline()
            doc.content("------------")
            doc.newline()
            doc.content("------------")
            doc.newline()
            for instance_path in sorted(instances_absolute_paths):
                with open(instance_path, "r") as instance_f:
                    instance_data = json.load(instance_f)
                subtitle = instance_path.split("/")[-1].replace('.jsonld', '')
                doc.heading(subtitle, char="-")
                doc.newline()
                doc.directive(name="admonition", arg="metadata sheet")
                field_list_indent = 3
                doc.newline()
                for prop, value in sorted(instance_data.items()):
                    if isinstance(value, (str, int, float)):
                        doc.field(name=prop, value=str(value), indent=field_list_indent)
                    elif isinstance(value, Dict):
                        if prop == "digitalIdentifier":
                            doc.field(name=prop, value=value["@id"], indent=field_list_indent)
                        if prop == "usedSpecies":
                            doc.field(name=prop, value=self._build_single_instance_link(value), indent=field_list_indent)
                        if prop == "hasTerminology":
                            if instance_data["hasTerminology"] and instance_data["hasTerminology"]["hasEntity"]:
                                parcellation_entities = instance_data["hasTerminology"]["hasEntity"]
                                doc.field(name=prop, value=self._build_instance_library_link(parcellation_entities), indent=field_list_indent)
                            else:
                                doc.field(name=prop, value="NOT DEFINED YET", indent=field_list_indent)
                    elif isinstance(value, List):
                        if all(isinstance(item, (str, int, float)) for item in value):
                            sorted_value_list = sorted([str(item) for item in value])
                            doc.field(name=prop, value=", ".join(sorted_value_list), indent=field_list_indent)
                        if all(isinstance(item, Dict) for item in value):
                            if prop == "hasVersion":
                                if instance_data["hasVersion"]:
                                    doc.field(name=prop, value=self._build_instance_library_link(value), indent=field_list_indent)
                                else:
                                    doc.field(name=prop, value="NOT DEFINED YET", indent=field_list_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <{title}_>`_")
                doc.newline()
                doc.content("------------")
                doc.newline()

    def build(self):
        for instancelib_docu_relative_path, instances_absolute_paths in self.relative_paths_for_instancelib_docu.items():
            # build RST docu for content types, licences and each terminology
            if instancelib_docu_relative_path.split("/")[0] in ["contentTypes", "licenses", "terminologies"]:
                self._build_simple_instances(instancelib_docu_relative_path, instances_absolute_paths)
            # build RST docu for research products and their versions (brainAtlases, commonCoordinateSpaces, brainAtlasVersions, commonCoordinateSpaceVersions)
            if instancelib_docu_relative_path.split("/")[0] in ["brainAtlases", "commonCoordinateSpaces", "brainAtlasVersions", "commonCoordinateSpaceVersions"]:
                self._build_complex_sands_instances(instancelib_docu_relative_path, instances_absolute_paths)
            # build RST docu for other instances (parcellationEntities, parcellationEntityVersions)
            if instancelib_docu_relative_path.split("/")[0] in ["parcellationEntities", "parcellationEntityVersions"]:
                self._build_simple_sands_instances(instancelib_docu_relative_path, instances_absolute_paths)
            else:
                pass
