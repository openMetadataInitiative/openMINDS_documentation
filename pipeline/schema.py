import json
import os.path
from typing import List, Optional, Dict

from rstcloth import RstCloth


class SchemaDocBuilder(object):

    def __init__(self, schema_file_path:str, root_path:str, relative_path_by_schema:Dict):
        _relative_path_without_extension = schema_file_path[len(root_path)+1:].replace(".schema.omi.json", "").split("/")
        self.version = _relative_path_without_extension[0]
        self.relative_path_without_extension = _relative_path_without_extension[1:]
        with open(schema_file_path, "r") as schema_f:
            self._schema_payload = json.load(schema_f)

    def _target_file_without_extension(self) -> str:
        return os.path.join(self.version, "docs", "specifications", "/".join(self.relative_path_without_extension))

    def build(self):
        target_file = os.path.join("target", f"{self._target_file_without_extension()}.rst")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        with open(target_file, "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            schema_name = self._schema_payload["name"]
            doc.heading(schema_name, char="#", overline=True)
            doc.newline()
            doc.heading(self._schema_payload["_type"], char="-")
            doc.newline()
            if "description" in self._schema_payload and self._schema_payload["description"]:
                doc.content(self._schema_payload["description"])
                doc.newline()
            semantic_equivalent = self._extract_semantic_equivalents()
            if semantic_equivalent:
                doc.field(name="Semantic equivalents:", value=semantic_equivalent)
                doc.newline()
            doc.content("------------")
            doc.newline()
            doc.content("------------")
            doc.newline()
            doc.heading("Properties", char="*", overline=True)
            doc.newline()
            doc.field(name="Required", value=self._extract_required_properties())
            doc.field(name="Optional", value=self._extract_optional_properties())
            doc.newline()
            doc.content("------------")
            doc.newline()
            if "properties" in self._schema_payload and self._schema_payload["properties"]:
                for p_qname, p_info in sorted(self._schema_payload["properties"].items()):
                    # property subsection title
                    p_name = p_info["name"]
                    doc.content(f".. _{p_name}_heading:")
                    doc.newline()
                    doc.heading(p_name, char="-")
                    doc.newline()
                    # property subsection description
                    if "description" in p_info.keys():
                        doc.content(p_info["description"])
                        doc.newline()
                    # property subsection specification box
                    doc.directive(name="admonition", arg="specifications")
                    doc.newline()
                    field_list_indent = 3
                    doc.field(name="semantic name", value=p_qname, indent=field_list_indent)
                    # multiline field list item for value types
                    value_specs = self.extract_value_specs(p_info)
                    field_name = "value type"
                    doc.field(name=field_name, value=value_specs[0], indent=field_list_indent)
                    if len(value_specs) > 1:
                        multiline_indent = len(field_name)+3+field_list_indent
                        doc.content(value_specs[1], indent=multiline_indent)
                    doc.field(name="instructions", value=p_info["_instruction"], indent=field_list_indent)
                    doc.newline()
                    doc.content(f"`BACK TO TOP <{schema_name}_>`_")
                    doc.newline()
                    doc.content("------------")
                    doc.newline()

    def _extract_required_properties(self) -> str:
        required_properties = []
        if "required" in self._schema_payload and self._schema_payload["required"]:
            for p in self._schema_payload["required"]:
                p_split = p.split("/")[-1]
                required_properties.append(f"`{p_split} <{p_split}_heading_>`_")
        return ", ".join(required_properties)

    def _extract_optional_properties(self) -> str:
        optional_properties = []
        if "properties" in self._schema_payload and self._schema_payload["properties"]:
            for p in self._schema_payload["properties"].keys():
                if "required" not in self._schema_payload or not self._schema_payload["required"] or p not in self._schema_payload["required"]:
                    p_split = p.split("/")[-1]
                    optional_properties.append(f"`{p_split} <{p_split}_heading_>`_")
        return ", ".join(optional_properties)

    def _extract_semantic_equivalents(self) -> Optional[str]:
        if "semanticEquivalent" in self._schema_payload:
            semantic_equivalents = []
            for se in self._schema_payload["semanticEquivalent"]:
                semantic_equivalents.append(se)
            return ", ".join(semantic_equivalents)
        return None

    def _identify_value_type(self, property) -> str:
        v_type = property["type"] if "type" in property else "object"
        if isinstance(v_type, list):
            if len(v_type) > 1:
                v_type = "or ".join([", ".join(v_type[:-1]), v_type[-1]])
        value_type = [v_type]
        if v_type == "array":
            i_type = property["items"]["type"] if "items" in property and "type" in property["items"] else "object"
            min_items = str(property["minItems"]) if "minItems" in property else "0"
            max_items = str(property["maxItems"]) if "maxItems" in property else "N"
            array_spec = f"\({min_items}-{max_items}\)"
            value_type = [i_type, v_type, array_spec]
        return " ".join(value_type)

    def _extract_edge_type(self, property):
        if "_embeddedTypes" in property:
            edge_type = "embedded"
        elif "_linkedTypes" in property:
            edge_type = "linked"
        else:
            edge_type = None
        return edge_type

    def _define_target_objects(self, object_list) -> str:
        if object_list:
            o_name_list = []
            for o in object_list:
                o_name = o.split('/')[-1]
                o_html_path = f"https://openminds-documentation.readthedocs.io/en/{self.version}/specifications/{self.relative_path_by_schema[o_name]}.html"
                o_name_list.append(f"`{o_name} <{o_html_path}>`_")
            if len(o_name_list) > 1:
                target_objects = " or ".join([", ".join(o_name_list[:-1]), o_name_list[-1]])
            else:
                target_objects = o_name_list[0]
            return target_objects
        return "undefined"

    def extract_value_specs(self, property):
        value_type = self._identify_value_type(property)
        if "object" in value_type:
            edge_type = self._extract_edge_type(property)
            v_1st_line = f"| {edge_type} {value_type} of type"
            target_objects = self._define_target_objects(property[f"_{edge_type}Types"])
            v_2nd_line = f"| {target_objects}"
            value_type = [v_1st_line, v_2nd_line]
        elif "string" in value_type:
            v_1st_line = f"| {value_type}"
            formatting = property["formatting"] if "formatting" in property else "undefined"
            multiline = "multiline" if "multiline" in property and property["multiline"] else "singleline"
            value_type = [v_1st_line, f"| formatting: {formatting}; {multiline}"]
        else:
            value_type = [f"{value_type}"]
        return value_type
