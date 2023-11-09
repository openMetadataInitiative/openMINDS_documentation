import json
import os.path
import re
from typing import List, Optional, Dict

from rstcloth import RstCloth


class InstancesDocBuilder(object):

    def __init__(self, instances_file_paths:List, version):
        self.version = version
        self.readthedocs_url = "https://openminds-documentation.readthedocs.io/en/"

        self.instances_collection = {}
        self.target_paths_for_instances = {}
        for instance_file_path in instances_file_paths:
            with open(instance_file_path, "r") as instance_f:
                instance_payload = json.load(instance_f)

            instance_id = instance_payload["@id"]

            split_path = instance_file_path.split("sources_instances")[-1].split("/")
            if split_path[3] in ["contentTypes", "licenses"]:
                relative_path = os.path.join("target", self.version, "docs", "instance_libraries", split_path[3])
            elif split_path[3] == "graphStructures" and split_path[6].endswith(".jsonld"):
                instance_shortName = instance_payload["shortName"]
                relative_path = os.path.join("target", self.version, "docs", "instance_libraries", split_path[4], instance_shortName)
            elif split_path[3] == "terminologies":
                relative_path = os.path.join("target", self.version, "docs", "instance_libraries", split_path[3], split_path[4])
            else:
                pass

            self.instances_collection[instance_id] = instance_payload
            if relative_path in self.target_paths_for_instances:
                self.target_paths_for_instances[relative_path].append(instance_id)
            else:
                self.target_paths_for_instances[relative_path] = [instance_id]

    def _build_single_term_link(self, termReference:Dict, instanceType:str) -> str:
        term_id = termReference["@id"]
        term = term_id.split("/")[-1].replace(".", "-").casefold()
        name = self.instances_collection[term_id]["name"] if "name" in self.instances_collection[term_id] else self.instances_collection[term_id]["shortName"]
        if instanceType == "licenses":
            linkdir = os.path.join(self.readthedocs_url, self.version, "instance_libraries")
        elif instanceType == "contentTypes":
            linkdir = os.path.join(self.readthedocs_url, self.version, "instance_libraries")
        else:
            linkdir = os.path.join(self.readthedocs_url, self.version, "instance_libraries", "terminologies")
        link = os.path.join(linkdir, f"{instanceType}.html#{term}")
        return f"`{name} <{link}>`_"

    def _build_multi_term_links(self, termReferenceList:List, instanceType:str) -> str:
        linklist = []
        for termReference in termReferenceList:
            linklist.append(self._build_single_term_link(termReference, instanceType))
        return ", ".join(linklist)

    def _build_single_version_link(self, versionReference:Dict, include_shortName=False) -> str:
        version_id = versionReference["@id"]
        id_label = version_id.split("/")[-1]
        label = id_label.split("_")[0]
        if version_id in self.instances_collection:
            version_data = self.instances_collection[version_id]
            title = version_data["shortName"]
            subtitle = version_data["versionIdentifier"] if "versionIdentifier" in version_data and version_data["versionIdentifier"] else id_label
            subtitle_url = subtitle.replace(' ', '-').replace(',', '-').replace('.', '-').replace('--', '-').casefold()
            title_mod = title.replace(' ', '%20')
            page = f"{title_mod}.html#version-{subtitle_url}"
            subdir = "brainAtlases" if "brainAtlasVersion" in version_id else "commonCoordinateSpaces"
            link = os.path.join(self.readthedocs_url, self.version, "instance_libraries", subdir, page)
            if include_shortName:
                return f"`{title} (version {subtitle}) <{link}>`_" if subtitle != id_label else f"{id_label} \(TODO\)"
            else:
                return f"`{subtitle} <{link}>`_" if subtitle != id_label else f"{id_label} \(TODO\)"
        else:
            return f"{id_label} \(TODO\)"

    def _build_multi_version_links(self, versionReferenceList:Dict, reverse_list=True, include_shortName=False) -> str:
        linklist = []
        for versionReference in versionReferenceList:
            linklist.append(self._build_single_version_link(versionReference, include_shortName))
        return list(reversed(sorted(linklist))) if reverse_list else sorted(linklist)

    def _build_simple_instances(self, docpath:str, instances_ids:List, schemadir:str):
        title = os.path.basename(docpath)
        title_CamelCase = "".join([title[0].capitalize(), title[1:]])
        schema_link = os.path.join(self.readthedocs_url, self.version, "schema_specifications", schemadir, f"{title}.html")
        with open(f"{docpath}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading(f"{title_CamelCase}", char="#", overline=True)
            doc.newline()
            doc.content(f"Related schema specification: `{title_CamelCase} <{schema_link}>`")
            doc.newline()
            doc.content("------------")
            doc.newline()
            doc.content("------------")
            doc.newline()
            for instance_id in sorted(instances_ids):
                instance_data = self.instances_collection[instance_id]
                subtitle = instance_id.split("/")[-1]
                doc.heading(subtitle, char="-")
                doc.newline()
                doc.directive(name="admonition", arg="metadata sheet")
                doc.newline()
                field_list_indent = 3
                for prop, value in sorted(instance_data.items()):
                    if type(value) == str:
                        doc.field(name=prop, value=str(value), indent=field_list_indent)
                    elif type(value) == List:
                        if all(isinstance(item, str) for item in value):
                            sorted_value_list = sorted(value)
                            doc.field(name=prop, value=", ".join(sorted_value_list), indent=field_list_indent)
                        if all(isinstance(item, Dict) for item in value):
                            doc.field(name=prop, value=self._build_multi_term_links(value, prop), indent=field_list_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <{title_CamelCase}_>`_")
                doc.newline()
                doc.content("------------")
                doc.newline()

    def _build_atlas_terminology(self, data:List) -> List:
        atlas_terminology = []
        for entity_ref in data:
            entity_data = self.instances_collection[entity_ref["@id"]]
            parents = entity_data.get('hasParent', [])
            if not parents:
                atlas_terminology.append(entity_data)
            else:
                for parent_ref in parents:
                    parent_item = self.instances_collection.get(parent_ref["@id"])
                    if parent_item:
                        parent_item.setdefault('children', []).append(entity_data)
        def build_bullet_list(tree, indent=0):
            bullet_list = []
            for item in tree:
                bullet_list.append(f"{'   '*(indent)}* {item['name']}")
                if 'children' in item:
                    subtree = build_bullet_list(item['children'], indent + 1)
                    bullet_list.extend(subtree)
            return bullet_list

        return build_bullet_list(atlas_terminology)

    def _build_brain_atlas(self, docpath:str, instance_id:str, schemadir:str):
        atlas_data = self.instances_collection[instance_id]
        title = os.path.basename(docpath)
        title_CamelCase = "".join([title[0].capitalize(), title[1:]])
        schema_link = os.path.join(self.readthedocs_url, self.version, "schema_specifications", f"{schemadir}.html")
        with open(f"{docpath}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading(f"{title}", char="#", overline=True)
            doc.newline()
            doc.content(f"Related schema specification: `BrainAtlas <{schema_link}>`_")
            doc.newline()
            doc.directive(name="admonition", arg="metadata sheet")
            doc.newline()
            field_list_indent = 3
            for prop, value in sorted(atlas_data.items()):
                if isinstance(value, (str, int, float)):
                    doc.field(name=prop, value=str(value), indent=field_list_indent)
                elif isinstance(value, Dict):
                    if prop == "digitalIdentifier":
                        doc.field(name=prop, value=value["@id"], indent=field_list_indent)
                    if prop == "usedSpecies":
                        doc.field(name=prop, value=self._build_single_term_link(value, "species"), indent=field_list_indent)
                    if prop == "hasTerminology":
                        doc.field(name=prop, value="(see below)", indent=field_list_indent)
                elif isinstance(value, List):
                    if all(isinstance(item, (str, int, float)) for item in value):
                        sorted_value_list = sorted([str(item) for item in value])
                        doc.field(name=prop, value=", ".join(sorted_value_list), indent=field_list_indent)
                    if all(isinstance(item, Dict) for item in value):
                        if prop == "hasVersion":
                            multiline_indent = len(prop) + 3 + field_list_indent
                            version_link_list = self._build_multi_version_links(atlas_data["hasVersion"])
                            doc.field(name=prop, value=f"| {version_link_list[0]}", indent=field_list_indent)
                            if len(version_link_list) > 1:
                                for link in version_link_list[1:]:
                                    doc.content(f"| {link}", indent=multiline_indent)
            doc.newline()
            if "hasTerminology" in atlas_data and atlas_data["hasTerminology"]:
                if "hasEntity" in atlas_data["hasTerminology"] and atlas_data["hasTerminology"]["hasEntity"]:
                    doc.heading(f"Terminology", char="#")
                    doc.newline()
                    parcellation_entities = atlas_data["hasTerminology"]["hasEntity"]
                    terminology = self._build_atlas_terminology(parcellation_entities)
                    if terminology:
                        for entity in terminology:
                            doc.content(entity)
            doc.newline()
            doc.content("------------")
            doc.newline()
            doc.content("------------")
            doc.newline()

            if "hasVersion" in atlas_data and atlas_data["hasVersion"]:
                atlas_version_list = [ref["@id"] for ref in atlas_data["hasVersion"]]
                for atlas_version_id in reversed(sorted(atlas_version_list)):
                    atlas_version_data = self.instances_collection[atlas_version_id] if atlas_version_id in self.instances_collection else None
                    subtitle = atlas_version_data["versionIdentifier"] if atlas_version_data else atlas_version_id.split("/")[-1].split("_")[-1]
                    doc.heading(f"version {subtitle}", char="#")
                    doc.newline()
                    if atlas_version_data:
                        for prop, value in sorted(atlas_version_data.items()):
                            if isinstance(value, (str, int, float)):
                                doc.field(name=prop, value=str(value), indent=field_list_indent)
                            elif isinstance(value, Dict):
                                if prop in ["digitalIdentifier", "relatedPublication"]:
                                    doc.field(name=prop, value=value["@id"], indent=field_list_indent)
                                if prop == "accessibility":
                                    doc.field(name=prop, value=self._build_single_term_link(value, "productAccessibility"), indent=field_list_indent)
                                if prop == "license":
                                    doc.field(name=prop, value=self._build_single_term_link(value, "licenses"), indent=field_list_indent)
                                if prop == "coordinateSpace":
                                    doc.field(name=prop, value=self._build_single_version_link(value, include_shortName=True), indent=field_list_indent)
                                if prop == "isNewVersionOf":
                                    doc.field(name=prop, value=self._build_single_version_link(value, include_shortName=True), indent=field_list_indent)
                                if prop == "type":
                                    doc.field(name=prop, value=self._build_single_term_link(value, "atlasType"), indent=field_list_indent)
                            elif isinstance(value, List):
                                if all(isinstance(item, (str, int, float)) for item in value):
                                    sorted_value_list = sorted([str(item) for item in value])
                                    doc.field(name=prop, value=", ".join(sorted_value_list), indent=field_list_indent)
                                if all(isinstance(item, Dict) for item in value):
                                    if prop == "isAlternativeVersionOf":
                                        multiline_indent = len(prop) + 3 + field_list_indent
                                        version_link_list = self._build_multi_version_links(value, include_shortName=True)
                                        doc.field(name=prop, value=f"| {version_link_list[0]}", indent=field_list_indent)
                                        if len(version_link_list) > 1:
                                            for link in version_link_list[1:]:
                                                doc.content(f"| {link}", indent=multiline_indent)
                    else:
                        doc.content(f"TODO")
                    doc.newline()
                    doc.content(f"`BACK TO TOP <{title}_>`_")
                    doc.newline()
                    doc.content("------------")
                    doc.newline()

    def _build_common_coordinate_space(self, docpath:str, instance_id:str, schemadir:str):
        space_data = self.instances_collection[instance_id]
        title = os.path.basename(docpath)
        title_CamelCase = "".join([title[0].capitalize(), title[1:]])
        schema_link = os.path.join(self.readthedocs_url, self.version, "schema_specifications", f"{schemadir}.html")
        with open(f"{docpath}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading(f"{title}", char="#", overline=True)
            doc.newline()
            doc.content(f"Related schema specification: `CommonCoordinateSpace <{schema_link}>`_")
            doc.newline()
            doc.directive(name="admonition", arg="metadata sheet")
            doc.newline()
            field_list_indent = 3
            for prop, value in sorted(space_data.items()):
                if isinstance(value, (str, int, float)):
                    doc.field(name=prop, value=str(value), indent=field_list_indent)
                elif isinstance(value, Dict):
                    if prop == "digitalIdentifier":
                        doc.field(name=prop, value=value["@id"], indent=field_list_indent)
                    if prop == "usedSpecies":
                        doc.field(name=prop, value=self._build_single_term_link(value, "species"), indent=field_list_indent)
                elif isinstance(value, List):
                    if all(isinstance(item, (str, int, float)) for item in value):
                        sorted_value_list = sorted([str(item) for item in value])
                        doc.field(name=prop, value=", ".join(sorted_value_list), indent=field_list_indent)
                    if all(isinstance(item, Dict) for item in value):
                        if prop == "hasVersion":
                            multiline_indent = len(prop) + 3 + field_list_indent
                            version_link_list = self._build_multi_version_links(space_data["hasVersion"])
                            doc.field(name=prop, value=f"| {version_link_list[0]}", indent=field_list_indent)
                            if len(version_link_list) > 1:
                                for link in version_link_list[1:]:
                                    doc.content(f"| {link}", indent=multiline_indent)
            doc.newline()
            doc.content("------------")
            doc.newline()
            doc.content("------------")
            doc.newline()

            if "hasVersion" in space_data and space_data["hasVersion"]:
                space_version_list = [ref["@id"] for ref in space_data["hasVersion"]]
                for space_version_id in reversed(sorted(space_version_list)):
                    space_version_data = self.instances_collection[space_version_id] if space_version_id in self.instances_collection else None
                    subtitle = space_version_data["versionIdentifier"] if space_version_data else space_version_id.split("/")[-1].split("_")[-1]
                    doc.heading(f"version {subtitle}", char="#")
                    doc.newline()
                    if space_version_data:
                        for prop, value in sorted(space_version_data.items()):
                            if isinstance(value, (str, int, float)):
                                doc.field(name=prop, value=str(value), indent=field_list_indent)
                            elif isinstance(value, Dict):
                                if prop in ["digitalIdentifier", "relatedPublication"]:
                                    doc.field(name=prop, value=value["@id"], indent=field_list_indent)
                                if prop == "accessibility":
                                    doc.field(name=prop, value=self._build_single_term_link(value, "productAccessibility"), indent=field_list_indent)
                                if prop == "license":
                                    doc.field(name=prop, value=self._build_single_term_link(value, "licenses"), indent=field_list_indent)
                                if prop == "anatomicalAxesOrientation":
                                    doc.field(name=prop, value=self._build_single_term_link(value, prop), indent=field_list_indent)
                                if prop == "nativeUnit":
                                    doc.field(name=prop, value=self._build_single_term_link(value, "UnitOfMeasurement"), indent=field_list_indent)
                                if prop == "isNewVersionOf":
                                    doc.field(name=prop, value=self._build_single_version_link(value, include_shortName=True), indent=field_list_indent)
                            elif isinstance(value, List):
                                if all(isinstance(item, (str, int, float)) for item in value):
                                    sorted_value_list = sorted([str(item) for item in value])
                                    doc.field(name=prop, value=", ".join(sorted_value_list), indent=field_list_indent)
                                if all(isinstance(item, Dict) for item in value):
                                    if prop == "isAlternativeVersionOf":
                                        multiline_indent = len(prop) + 3 + field_list_indent
                                        version_link_list = self._build_multi_version_links(value, include_shortName=True)
                                        doc.field(name=prop, value=f"| {version_link_list[0]}", indent=field_list_indent)
                                        if len(version_link_list) > 1:
                                            for link in version_link_list[1:]:
                                                doc.content(f"| {link}", indent=multiline_indent)
                    else:
                        doc.content(f"TODO")
                    doc.newline()
                    doc.content(f"`BACK TO TOP <{title}_>`_")
                    doc.newline()
                    doc.content("------------")
                    doc.newline()

    def build(self):
        for page_path, instances_ids in self.target_paths_for_instances.items():
            os.makedirs(os.path.dirname(page_path), exist_ok=True)
            # build RST docu for each terminology
            if "terminologies" in page_path:
                self._build_simple_instances(page_path, instances_ids, "controlledTerms")
            # build RST docu for content types
            elif "contentTypes" in page_path:
                self._build_simple_instances(page_path, instances_ids, "core/data/contentType")
            # # build RST docu for licenses
            elif "licenses" in page_path:
                self._build_simple_instances(page_path, instances_ids, "core/data/license")
            # build RST docu for each brain atlas
            elif "brainAtlases" in page_path:
                self._build_brain_atlas(page_path, instances_ids[0], "SANDS/atlas/brainAtlas")
            # build RST docu for each brain atlas
            elif "commonCoordinateSpaces" in page_path:
                self._build_common_coordinate_space(page_path, instances_ids[0], "SANDS/atlas/commonCoordinateSpace")
            else:
                pass
