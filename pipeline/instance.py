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

    def _build_single_term_link(self, termReference:Dict, terminology:str) -> str:
        term = termReference["@id"].split("/")[-1]
        name = self.instances_libraries["terminologies"][terminology][term]["name"]
        name_mod = name.replace(' ', '-').casefold()
        link = os.path.join(self.readthedocs_url, self.version, "libraries", "terminologies", f"{terminology}.html#{name_mod}")
        return f"`{name} <{link}>`_"

    def _build_multi_term_links(self, termReferenceList:List, terminology:str) -> str:
        linklist = []
        for termReference in termReferenceList:
            linklist.append(self._build_single_term_link(termReference, terminology))
        return ", ".join(linklist)

    # def _build_product_version_links(self, versions:Dict, productType:str) -> str:
    #     linklist = []
    #     for name, vdict  in sorted(versions.items()):
    #         vdata = vdict["atlas"] if productType == "brainAtlases" else vdict
    #         vID = vdata['versionIdentifier']
    #         vID_mod = vID.replace(' ', '-').replace(',', '-').replace('.', '-').casefold()
    #         space_html_title = f"{vdata['shortName'].replace(' ', '%20')}.html#version-{vID_mod}"
    #         link = os.path.join(self.readthedocs_url, self.version, "libraries", productType, space_html_title)
    #         linklist.append(f"`{vID} <{link}>`_")
    #     return ", ".join(linklist)

    def _build_single_version_link(self, versionReference:Dict, versions:Dict, title:str) -> str:
        vname = versionReference["@id"].split("/")[-1]
        if "brainAtlasVersion" in versionReference["@id"]:
            name = versions[vname]["atlas"]["versionIdentifier"] if vname in versions and versions[vname]["atlas"] else vname
            subdir = "brainAtlases"
        else:
            name = versions[vname]["versionIdentifier"] if vname in versions and versions[vname] else vname
            subdir = "commonCoordinateSpaces"
        title_mod = title.replace(' ', '%20')
        name_mod = name.replace(' ', '-').replace(',', '-').replace('.', '-').replace('--', '-').casefold()
        page = f"{title_mod}.html#version-{name_mod}"
        link = os.path.join(self.readthedocs_url, self.version, "libraries", subdir, page)
        return f"`{name} <{link}>`_" if name != vname else f"{name} \(TODO\)"

    def _build_multi_version_links(self, versionReferenceList:Dict, versions:Dict, title:str, reversed=True) -> str:
        linklist = []
        for versionReference in versionReferenceList:
            linklist.append(self._build_single_version_link(versionReference, versions, title))
        return list(reversed(sorted(linklist))) if reversed else sorted(linklist)

    def _build_terminology(self, target_file:str, title:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            name_CamelCase = "".join([title[0].capitalize(), title[1:]])
            doc.heading(f"{name_CamelCase}", char="#", overline=True)
            doc.newline()
            schema_link = os.path.join(self.readthedocs_url, self.version, "specifications", "controlledTerms", f"{title}.html")
            doc.content(f"All instances listed below can be validated against the `{name_CamelCase} <{schema_link}>`_ schema specification.")
            doc.newline()
            doc.content("------------")
            doc.newline()
            doc.content("------------")
            doc.newline()
            for term_name, term_data in sorted(data_to_display.items()):
                doc.heading(term_data["name"], char="-")
                doc.newline()
                doc.directive(name="admonition", arg="metadata sheet")
                doc.newline()
                field_list_indent = 3
                doc.field(name="semantic name", value=term_data['@id'], indent=field_list_indent)
                definition = term_data["definition"] if "definition" in term_data and term_data["definition"] else "\-"
                doc.field(name="definition", value=definition, indent=field_list_indent)
                description = term_data["description"] if "description" in term_data and term_data["description"] else "\-"
                doc.field(name="description", value=description, indent=field_list_indent)
                synonym = ", ".join(term_data["synonym"]) if "synonym" in term_data and term_data["synonym"] else "\-"
                doc.field(name="synonyms", value=synonym, indent=field_list_indent)
                doc.content("------------", indent=field_list_indent)
                ontologyID = term_data["preferredOntologyIdentifier"] if "preferredOntologyIdentifier" in term_data and term_data["preferredOntologyIdentifier"] else "\-"
                doc.field(name="preferred ontology ID", value=ontologyID, indent=field_list_indent)
                interlexID = term_data["interlexIdentifier"] if "interlexIdentifier" in term_data and term_data["interlexIdentifier"] else "\-"
                doc.field(name="InterLex ID", value=interlexID, indent=field_list_indent)
                ksEntry = term_data["knowledgeSpaceLink"] if "knowledgeSpaceLink" in term_data and term_data["knowledgeSpaceLink"] else "\-"
                doc.field(name="KnowledgeSpace entry", value=ksEntry, indent=field_list_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <{title}_>`_")
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
                doc.directive(name="admonition", arg="metadata sheet")
                doc.newline()
                field_list_indent = 3
                doc.field(name="semantic name", value=ct_data["@id"], indent=field_list_indent)
                displaylabel = ct_data["displayLabel"] if "displayLabel" in ct_data and ct_data["displayLabel"] else "\-"
                doc.field(name="display label", value=displaylabel, indent=field_list_indent)
                extensions = ", ".join(ct_data["fileExtension"]) if "fileExtension" in ct_data and ct_data["fileExtension"] else "\-"
                doc.field(name="file extensions", value=extensions, indent=field_list_indent)
                synonyms = ", ".join(ct_data["synonym"]) if "synonym" in ct_data and ct_data["synonym"] else "\-"
                doc.field(name="synonyms", value=synonyms, indent=field_list_indent)
                description = ct_data["description"] if "description" in ct_data and ct_data["description"] else "\-"
                doc.field(name="description", value=description, indent=field_list_indent)
                specification = ct_data["specification"] if "specification" in ct_data and ct_data["specification"] else "\-"
                doc.field(name="specification", value=specification, indent=field_list_indent)
                datatypes = self._build_multi_term_links(ct_data["dataType"], "dataType") if "dataType" in ct_data and ct_data["dataType"] else "\-"
                doc.field(name="data types", value=datatypes, indent=field_list_indent)
                mediatype = ct_data["relatedMediaType"] if "relatedMediaType" in ct_data and ct_data["relatedMediaType"] else "\-"
                doc.field(name="related media type", value=mediatype, indent=field_list_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <ContentTypes_>`_")
                doc.newline()
                doc.content("------------")
                doc.newline()

    def _build_licenses(self, target_file:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading("Licenses", char="#", overline=True)
            doc.newline()
            for license_name, license_data in sorted(data_to_display.items()):
                doc.heading(license_data["shortName"], char="-")
                doc.newline()
                doc.directive(name="admonition", arg="metadata sheet")
                doc.newline()
                field_list_indent = 3
                doc.field(name="semantic name", value=license_data["@id"], indent=field_list_indent)
                fullName = license_data["fullName"] if "fullName" in license_data and license_data["fullName"] else "\-"
                doc.field(name="full name", value=fullName, indent=field_list_indent)
                legalCode = license_data["legalCode"] if "legalCode" in license_data and license_data["legalCode"] else "\-"
                doc.field(name="legal code", value=legalCode, indent=field_list_indent)
                webpage = license_data["webpage"] if "webpage" in license_data and license_data["webpage"] else "\-"
                field_name = "webpages"
                doc.field(name=field_name, value=webpage[0], indent=field_list_indent)
                if len(webpage) > 1:
                    multiline_indent = len(field_name) + 3 + field_list_indent
                    doc.content(webpage[1], indent=multiline_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <Licenses_>`_")
                doc.newline()
                doc.content("------------")
                doc.newline()

    def _build_atlas_terminology(self, data:Dict) -> List:
        atlas_terminology = []
        for entity in data.values():
            parents = entity.get('hasParent', [])
            if not parents:
                atlas_terminology.append(entity)
            else:
                for parent_ref in parents:
                    parent_item = data.get(parent_ref["@id"].split("/")[-1])
                    if parent_item:
                        parent_item.setdefault('children', []).append(entity)
        def build_bullet_list(tree, indent=0):
            bullet_list = []
            for item in tree:
                bullet_list.append(f"{'   '*(indent)}* {item['name']}")
                if 'children' in item:
                    subtree = build_bullet_list(item['children'], indent + 1)
                    bullet_list.extend(subtree)
            return bullet_list

        return build_bullet_list(atlas_terminology)

    def _build_brain_atlas(self, target_file:str, title:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            data = data_to_display["atlas"]
            doc = RstCloth(output_file, line_width=100000)
            doc.heading(f"{title}", char="#", overline=True)
            doc.newline()
            doc.directive(name="admonition", arg="metadata sheet")
            doc.newline()
            field_list_indent = 3
            doc.field(name="semantic name", value=data["@id"], indent=field_list_indent)
            d_fullName = data["fullName"] if "fullName" in data and data["fullName"] else "\-"
            doc.field(name="full name", value=d_fullName, indent=field_list_indent)
            d_abbr = data["abbreviation"] if "abbreviation" in data and data["abbreviation"] else "\-"
            doc.field(name="abbreviation", value=d_abbr, indent=field_list_indent)
            d_species = self._build_single_term_link(data["usedSpecies"], "species") if "usedSpecies" in data and data["usedSpecies"] else "\-"
            doc.field(name="used species", value=d_species, indent=field_list_indent)
            d_digitalID = data["digitalIdentifier"]["@id"] if "digitalIdentifier" in data and data["digitalIdentifier"] else "\-"
            doc.field(name="digital ID", value=d_digitalID, indent=field_list_indent)
            d_ontologyID = data["ontologyIdentifier"] if "ontologyIdentifier" in data and data["ontologyIdentifier"] else "\-"
            doc.field(name="ontology ID", value=d_ontologyID, indent=field_list_indent)
            d_homepage = data["homepage"] if "homepage" in data and data["homepage"] else "\-"
            doc.field(name="homepage", value=d_homepage, indent=field_list_indent)
            d_citation = data["howToCite"] if "howToCite" in data and data["howToCite"] else "\-"
            doc.field(name="howToCite", value=d_citation, indent=field_list_indent)
            if "hasVersion" in data and data["hasVersion"]:
                field_name = "has versions"
                multiline_indent = len(field_name)+3+field_list_indent
                version_link_list = self._build_multi_version_links(data["hasVersion"], data_to_display["versions"], title)
                doc.field(name=field_name, value=f"| {version_link_list[0]}", indent=field_list_indent)
                if len(version_link_list) > 1:
                    for link in version_link_list[1:]:
                        doc.content(f"| {link}", indent=multiline_indent)
                doc.newline()
                doc.heading(f"Terminology", char="#")
                if "parcellation_entities" in data_to_display and data_to_display["parcellation_entities"]:
                    atlas_terminology_list = self._build_atlas_terminology(data_to_display["parcellation_entities"])
                    if atlas_terminology_list:
                        for term in atlas_terminology_list:
                            doc.content(term)
                doc.newline()
                doc.content("------------")
                doc.newline()
                doc.content("------------")
                doc.newline()

                for _, vdict in sorted(data_to_display["versions"].items()):
                    vdata = vdict["atlas"]
                    subtitle = vdata['versionIdentifier']
                    doc.heading(f"version {subtitle}", char="#")
                    doc.newline()
                    doc.directive(name="admonition", arg="metadata sheet")
                    doc.newline()
                    field_list_indent = 3
                    doc.field(name="semantic name", value=vdata["@id"], indent=field_list_indent)
                    if "isNewVersionOf" in vdata and vdata["isNewVersionOf"]:
                        old_version_link = self._build_single_version_link(vdata["isNewVersionOf"], data_to_display["versions"], title)
                        doc.field(name="previous version", value=old_version_link, indent=field_list_indent)
                    if "isAlternativeVersionOf" in vdata and vdata["isAlternativeVersionOf"]:
                        field_name = "alternative versions"
                        multiline_indent = len(field_name)+3+field_list_indent
                        alt_version_link_list = self._build_multi_version_links(vdata["isAlternativeVersionOf"], data_to_display["versions"], title)
                        doc.field(name=field_name, value=alt_version_link_list[0], indent=field_list_indent)
                        if len(alt_version_link_list) > 1:
                            for link in alt_version_link_list[1:]:
                                doc.content(f"| {link}", indent=multiline_indent)
                    dv_fullName = vdata["fullName"] if "fullName" in vdata and vdata["fullName"] else "\-"
                    if dv_fullName != d_fullName:
                        doc.field(name="full name", value=dv_fullName, indent=field_list_indent)
                    dv_abbr = vdata["abbreviation"] if "abbreviation" in vdata and vdata["abbreviation"] else "\-"
                    if dv_abbr != d_abbr:
                        doc.field(name="abbreviation", value=dv_abbr, indent=field_list_indent)
                    dv_digitalID = vdata["digitalIdentifier"] if "digitalIdentifier" in vdata and vdata["digitalIdentifier"] else "\-"
                    doc.field(name="digital ID", value=dv_digitalID, indent=field_list_indent)
                    dv_ontologyID = vdata["ontologyIdentifier"] if "ontologyIdentifier" in vdata and vdata["ontologyIdentifier"] else "\-"
                    doc.field(name="ontology ID", value=dv_ontologyID, indent=field_list_indent)
                    dv_homepage = vdata["homepage"] if "homepage" in vdata and vdata["homepage"] else "\-"
                    if dv_homepage != d_homepage:
                        doc.field(name="homepage", value=dv_homepage, indent=field_list_indent)
                    dv_citation = vdata["howToCite"] if "howToCite" in vdata and vdata["howToCite"] else "\-"
                    doc.field(name="howToCite", value=dv_citation, indent=field_list_indent)
                    dv_access = self._build_single_term_link(vdata["accessibility"], "productAccessibility") if "accessibility" in vdata and vdata["accessibility"] else "\-"
                    doc.field(name="accessibility", value=dv_access, indent=field_list_indent)
                    doc.newline()
                    doc.content(f"`BACK TO TOP <{title}_>`_")
                    doc.newline()
                    doc.content("------------")
                    doc.newline()

    def _build_common_coordinate_space(self, target_file:str, title:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            data = data_to_display["space"]
            doc = RstCloth(output_file, line_width=100000)
            doc.heading(f"{title}", char="#", overline=True)
            doc.newline()
            doc.directive(name="admonition", arg="metadata sheet")
            doc.newline()
            field_list_indent = 3
            doc.field(name="semantic name", value=data["@id"], indent=field_list_indent)
            d_fullName = data["fullName"] if "fullName" in data and data["fullName"] else "\-"
            doc.field(name="full name", value=d_fullName, indent=field_list_indent)
            d_abbr = data["abbreviation"] if "abbreviation" in data and data["abbreviation"] else "\-"
            doc.field(name="abbreviation", value=d_abbr, indent=field_list_indent)
            d_species = self._build_single_term_link(data["usedSpecies"], "species") if "usedSpecies" in data and data["usedSpecies"] else "\-"
            doc.field(name="used species", value=d_species, indent=field_list_indent)
            d_digitalID = data["digitalIdentifier"] if "digitalIdentifier" in data and data["digitalIdentifier"] else "\-"
            doc.field(name="digital ID", value=d_digitalID, indent=field_list_indent)
            d_ontologyID = data["ontologyIdentifier"] if "ontologyIdentifier" in data and data["ontologyIdentifier"] else "\-"
            doc.field(name="ontology ID", value=d_ontologyID, indent=field_list_indent)
            d_homepage = data["homepage"] if "homepage" in data and data["homepage"] else "\-"
            doc.field(name="homepage", value=d_homepage, indent=field_list_indent)
            d_citation = data["howToCite"] if "howToCite" in data and data["howToCite"] else "\-"
            doc.field(name="howToCite", value=d_citation, indent=field_list_indent)
            if "hasVersion" in data and data["hasVersion"]:
                field_name = "has versions"
                multiline_indent = len(field_name)+3+field_list_indent
                version_link_list = self._build_multi_version_links(data["hasVersion"], data_to_display["versions"], title)
                doc.field(name=field_name, value=f"| {version_link_list[0]}", indent=field_list_indent)
                if len(version_link_list) > 1:
                    for link in version_link_list[1:]:
                        doc.content(f"| {link}", indent=multiline_indent)
                doc.newline()
                doc.content("------------")
                doc.newline()
                doc.content("------------")
                doc.newline()
                for _, vdata in sorted(data_to_display["versions"].items()):
                    subtitle = vdata['versionIdentifier']
                    doc.heading(f"version {subtitle}", char="#")
                    doc.newline()
                    doc.directive(name="admonition", arg="metadata sheet")
                    doc.newline()
                    field_list_indent = 3
                    doc.field(name="semantic name", value=vdata["@id"], indent=field_list_indent)
                    if "isNewVersionOf" in vdata and vdata["isNewVersionOf"]:
                        old_version_link = self._build_single_version_link(vdata["isNewVersionOf"], data_to_display["versions"], title)
                        doc.field(name="previous version", value=old_version_link, indent=field_list_indent)
                    if "isAlternativeVersionOf" in vdata and vdata["isAlternativeVersionOf"]:
                        field_name = "alternative versions"
                        multiline_indent = len(field_name)+3+field_list_indent
                        alt_version_link_list = self._build_multi_version_links(vdata["isAlternativeVersionOf"], data_to_display["versions"], title)
                        doc.field(name=field_name, value=alt_version_link_list[0], indent=field_list_indent)
                        if len(alt_version_link_list) > 1:
                            for link in alt_version_link_list[1:]:
                                doc.content(f"| {link}", indent=multiline_indent)
                    dv_fullName = vdata["fullName"] if "fullName" in vdata and vdata["fullName"] else "\-"
                    if dv_fullName != d_fullName:
                        doc.field(name="full name", value=dv_fullName, indent=field_list_indent)
                    dv_abbr = vdata["abbreviation"] if "abbreviation" in vdata and vdata["abbreviation"] else "\-"
                    if dv_abbr != d_abbr:
                        doc.field(name="abbreviation", value=dv_abbr, indent=field_list_indent)
                    dv_digitalID = vdata["digitalIdentifier"] if "digitalIdentifier" in vdata and vdata["digitalIdentifier"] else "\-"
                    doc.field(name="digital ID", value=dv_digitalID, indent=field_list_indent)
                    dv_ontologyID = vdata["ontologyIdentifier"] if "ontologyIdentifier" in vdata and vdata["ontologyIdentifier"] else "\-"
                    doc.field(name="ontology ID", value=dv_ontologyID, indent=field_list_indent)
                    dv_homepage = vdata["homepage"] if "homepage" in vdata and vdata["homepage"] else "\-"
                    if dv_homepage != d_homepage:
                        doc.field(name="homepage", value=dv_homepage, indent=field_list_indent)
                    dv_citation = vdata["howToCite"] if "howToCite" in vdata and vdata["howToCite"] else "\-"
                    doc.field(name="howToCite", value=dv_citation, indent=field_list_indent)
                    dv_access = self._build_single_term_link(vdata["accessibility"], "productAccessibility") if "accessibility" in vdata and vdata["accessibility"] else "\-"
                    doc.field(name="accessibility", value=dv_access, indent=field_list_indent)
                    dv_released = vdata["releaseDate"] if "releaseDate" in vdata and vdata["releaseDate"] else "\-"
                    doc.field(name="release date", value=dv_released, indent=field_list_indent)
                    dv_aax = self._build_single_term_link(vdata["anatomicalAxesOrientation"], "anatomicalAxesOrientation") if "anatomicalAxesOrientation" in vdata and vdata["anatomicalAxesOrientation"] else "\-"
                    doc.field(name="anatomical axis orientation", value=dv_aax, indent=field_list_indent)
                    dv_unit = self._build_single_term_link(vdata["nativeUnit"], "unitOfMeasurement") if "nativeUnit" in vdata and vdata["nativeUnit"] else "\-"
                    doc.field(name="native unit", value=dv_unit, indent=field_list_indent)
                    doc.newline()
                    doc.content(f"`BACK TO TOP <{title}_>`_")
                    doc.newline()
                    doc.content("------------")
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
            ba_title = ba_data["atlas"]["shortName"]
            target_file = self._target_file_without_extension("/".join(["brainAtlases", ba_title]))
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            self._build_brain_atlas(target_file, ba_title, ba_data)

        # build RST docu for each common coordinate space
        for ccs_name, ccs_data in self.instances_libraries["commonCoordinateSpaces"].items():
            ccs_title = ccs_data["space"]["shortName"]
            target_file = self._target_file_without_extension("/".join(["commonCoordinateSpaces", ccs_title]))
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            self._build_common_coordinate_space(target_file, ccs_title, ccs_data)
