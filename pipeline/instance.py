import json
import os.path
import re
from typing import List, Optional, Dict

from rstcloth import RstCloth


class InstancesLibraryBuilder(object):

    def __init__(self):
        self.instances_libraries = {
            "terminologies": {},
            "contentTypes": {},
            "licenses": {},
            "brainAtlases": {},
            "commonCoordinateSpaces": {},
            "_common": {}
        }
    def load_instance(self, instance_file_path:str, root_path:str):
        _relative_path_without_extension = instance_file_path[len(root_path)+1:].replace(".jsonld", "").split("/")
        self.relative_path_without_extension = "/".join(_relative_path_without_extension[1:])
        self.instance_basename = os.path.basename(self.relative_path_without_extension)
        with open(instance_file_path, "r") as instance_f:
            self._instance_payload = json.load(instance_f)

    def _add_instance_to_terminologies_libraries(self):
        terminology_name = self.relative_path_without_extension.split("/")[1]
        if terminology_name in self.instances_libraries["terminologies"]:
            self.instances_libraries["terminologies"][terminology_name][self.instance_basename] = self._instance_payload
        else:
            self.instances_libraries["terminologies"][terminology_name] = {
                self.instance_basename: self._instance_payload
            }

    def _add_instance_to_content_types_library(self):
        self.instances_libraries["contentTypes"][self.instance_basename] = self._instance_payload

    def _add_instance_to_licenses_library(self):
        self.instances_libraries["licenses"][self.instance_basename] = self._instance_payload

    def _add_instance_to_common(self):
        common_type = self.relative_path_without_extension.split("/")[2]
        if common_type in self.instances_libraries["_common"]:
            self.instances_libraries["_common"][common_type][self.instance_basename] = self._instance_payload

    def _add_instance_to_brainAtlases_libraries(self):
        ba_name = self.relative_path_without_extension.split("/")[2]
        if ba_name not in self.instances_libraries["brainAtlases"]:
            self.instances_libraries["brainAtlases"][ba_name] = {
                "atlas": None,
                "parcellation_entities": {},
                "versions": {}
            }
        if ba_name == self.instance_basename:
            self.instances_libraries["brainAtlases"][ba_name]["atlas"] = self._instance_payload
        else:
            if f"/parcellationEntities/{ba_name}" in self.relative_path_without_extension:
                pe_name = self.instance_basename
                self.instances_libraries["brainAtlases"][ba_name]["parcellation_entities"][pe_name] = self._instance_payload
            if f"/versions/{ba_name}" in self.relative_path_without_extension:
                bav_name = self.relative_path_without_extension.split("/")[4]
                bav_id = bav_name.split("_")[-1]
                if bav_name not in self.instances_libraries["brainAtlases"][ba_name]["versions"]:
                    self.instances_libraries["brainAtlases"][ba_name]["versions"][bav_name] = {
                        "atlas": None,
                        "parcellation_entities": {}
                    }
                if bav_name == self.instance_basename:
                    self.instances_libraries["brainAtlases"][ba_name]["versions"][bav_name]["atlas"] = self._instance_payload
                else:
                    if f"/parcellationEntities_{bav_id}/" in self.relative_path_without_extension:
                        pev_name = self.instance_basename
                        self.instances_libraries["brainAtlases"][ba_name]["versions"][bav_name]["parcellation_entities"][pev_name] = self._instance_payload

    def _add_instance_to_common_coordinate_space_libraries(self):
        ccs_name = self.relative_path_without_extension.split("/")[2]
        if ccs_name not in self.instances_libraries["commonCoordinateSpaces"]:
            self.instances_libraries["commonCoordinateSpaces"][ccs_name] = {
                "space": None,
                "versions": {}
            }
        if ccs_name == self.instance_basename:
            self.instances_libraries["commonCoordinateSpaces"][ccs_name]["space"] = self._instance_payload
        else:
            if f"versions/{ccs_name}" in self.relative_path_without_extension:
                ccsv_name = self.instance_basename
                self.instances_libraries["commonCoordinateSpaces"][ccs_name]["versions"][ccsv_name] = self._instance_payload

    def add_instance_to_library(self):
        if self.relative_path_without_extension.startswith("terminologies"):
            self._add_instance_to_terminologies_libraries()
        if self.relative_path_without_extension.startswith("contentTypes"):
            self._add_instance_to_content_types_library()
        if self.relative_path_without_extension.startswith("licenses"):
            self._add_instance_to_licenses_library()
        if self.relative_path_without_extension.startswith("graphStructures/common"):
            self._add_instance_to_common()
        if self.relative_path_without_extension.startswith("graphStructures/brainAtlases"):
            self._add_instance_to_brainAtlases_libraries()
        if self.relative_path_without_extension.startswith("graphStructures/commonCoordinateSpaces"):
            self._add_instance_to_common_coordinate_space_libraries()

class InstancesDocBuilder(object):

    def __init__(self, instances_version:str, instances_libraries:Dict):
        self.readthedocs_url = "https://openminds-documentation.readthedocs.io/en/"
        self.version = instances_version
        self.instances_libraries = instances_libraries

    def _target_file_without_extension(self, target_basename:str) -> str:
        return os.path.join("target", self.version, "docs", "libraries", f"{target_basename}")

    def _build_terminology(self, target_file:str, name:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            name = "".join([name[0].capitalize(), name[1:]])
            doc.heading(f"{name}", char="#", overline=True)
            doc.newline()
            doc.content("------------")
            doc.newline()
            doc.content("------------")
            doc.newline()
            for term_name, term_data in sorted(data_to_display.items()):
                doc.heading(term_data["name"], char="-")
                doc.newline()
                doc.directive(name="admonition", arg=f"``{term_data['@id']}``")
                doc.newline()
                field_list_indent = 3
                definition = term_data["definition"] if "definition" in term_data and term_data["definition"] else "\-"
                doc.field(name="definition", value=definition, indent=field_list_indent)
                synonym = ", ".join(term_data["synonym"]) if "synonym" in term_data and term_data["synonym"] else "\-"
                doc.field(name="synonyms", value=synonym, indent=field_list_indent)
                ontologyID = term_data["preferredOntologyIdentifier"] if "preferredOntologyIdentifier" in term_data and term_data["preferredOntologyIdentifier"] else "\-"
                doc.field(name="preferred ontology ID", value=ontologyID, indent=field_list_indent)
                interlexID = term_data["interlexIdentifier"] if "interlexIdentifier" in term_data and term_data["interlexIdentifier"] else "\-"
                doc.field(name="InterLex ID", value=interlexID, indent=field_list_indent)
                ksEntry = term_data["knowledgeSpaceLink"] if "knowledgeSpaceLink" in term_data and term_data["knowledgeSpaceLink"] else "\-"
                doc.field(name="KnowledgeSpace entry", value=ksEntry, indent=field_list_indent)
                description = term_data["description"] if "description" in term_data and term_data["description"] else "\-"
                doc.field(name="description", value=description, indent=field_list_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <{name}_>`_")
                doc.newline()
                doc.content("------------")
                doc.newline()

    def _build_content_types(self, target_file:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading("ContentTypes", char="#", overline=True)
            doc.newline()
            for ct_name, ct_data in sorted(data_to_display.items()):
                doc.heading(ct_data["name"], char="-")
                doc.newline()

    def _build_licenses(self, target_file:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading("Licenses", char="#", overline=True)
            doc.newline()
            for license_name, license_data in sorted(data_to_display.items()):
                doc.heading(license_data["fullName"], char="-")
                doc.newline()

    def _build_brain_atlas(self, target_file:str, name:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading(f"{name}", char="#", overline=True)
            doc.newline()

    def _build_common_coordinate_space(self, target_file:str, name:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading(f"{name}", char="#", overline=True)
            doc.newline()

    def build(self):
        # build RST docu for each terminology
        for terminology_name, terms in self.instances_libraries["terminologies"].items():
            target_file = self._target_file_without_extension("/".join(["terminologies", terminology_name]))
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            self._build_terminology(target_file, terminology_name, terms)

        # build RST docu for content types
        target_file = self._target_file_without_extension("contentTypes")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        self._build_content_types(target_file, self.instances_libraries["contentTypes"])

        # build RST docu for licenses
        target_file = self._target_file_without_extension("licenses")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        self._build_licenses(target_file, self.instances_libraries["licenses"])

        # build RST docu for each brain atlas
        for ba_name, ba_data in self.instances_libraries["brainAtlases"].items():
            target_file = self._target_file_without_extension("/".join(["brainAtlases", ba_name]))
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            self._build_brain_atlas(target_file, ba_name, ba_data)

        # build RST docu for each common coordinate space
        for ccs_name, ccs_data in self.instances_libraries["commonCoordinateSpaces"].items():
            target_file = self._target_file_without_extension("/".join(["commonCoordinateSpaces", ccs_name]))
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            self._build_common_coordinate_space(target_file, ccs_name, ccs_data)