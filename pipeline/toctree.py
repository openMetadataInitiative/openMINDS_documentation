import os.path
from typing import List

from rstcloth import RstCloth
from pipeline.utils import count_instances

def create_toc_tree_page(version:str, relative_path:List[str]):
    target_file = os.path.join("target", f"{version}/docs/{'/'.join(relative_path)}.rst")
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    with open(target_file, "w") as output_file:
        doc = RstCloth(output_file, line_width=160)
        heading = ''.join([relative_path[-1][0].upper(), relative_path[-1][1:]]).replace("_", " ")
        doc.heading(heading, char="#", overline=True)
        doc.newline()
        # TODO add some description -> but where does it come from?
        links = []
        tree_items = []
        sub_dirs = sorted(os.listdir(os.path.join("target", version, "docs", "/".join(relative_path))), key=str.casefold)
        for sub_dir in sub_dirs:
            sub_dir = sub_dir.replace(".rst", "")
            links.append(f"- `{sub_dir[0].upper()}{sub_dir[1:]} <{relative_path[-1]}/{sub_dir.replace(' ', '%20')}.html>`_")
            tree_items.append(f"{relative_path[-1]}/{sub_dir}")
            sub_dir_path = os.path.join("target", version, "docs", "/".join(relative_path), sub_dir)
            if os.path.isdir(sub_dir_path):
                sub_dirs_of_sub_dir = os.listdir(sub_dir_path)
                if sub_dirs_of_sub_dir:
                    new_relative_path = []
                    new_relative_path.extend(relative_path)
                    new_relative_path.append(sub_dir)
                    create_toc_tree_page(version, new_relative_path)

        if heading == "Instance libraries":
            instances_count = count_instances(version)
            doc.note(content=["The instance libraries are continuously extended and optimized.",
            "You can request the registration of new instances or corrections\/extensions of existing",
            "instances by raising an issue on `openMINDS_instances <https://github.com/HumanBrainProject/openMINDS_instances/issues>`_",
            "",
            f"The {version} version of openMINDS contains {instances_count} metadata instances in total. The "])

        for link in links:
            doc.content(link)

        doc.newline()
        doc.content(f".. toctree::")
        doc.newline()
        for tree_item in tree_items:
            doc.content(tree_item, indent=3)
