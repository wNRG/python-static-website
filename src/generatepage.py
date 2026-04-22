import os

from markdown_to_html import markdown_to_html_node
from extractmarkdown import extract_title
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from {from_path} to {dest_path} using {template_path}...")
    markdown_file = ""
    template_file = ""
    
    with open(from_path, "r") as f:
        markdown_file = f.read()

    with open(template_path, "r") as f:
        template_file = f.read()

    html_string = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)
    
    x = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(x)
    
def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)

    for file in files:
        dir_path = os.path.join(dir_path_content, file)
        if os.path.isfile(dir_path):
            html_file = Path(file).with_suffix(".html")
            dest_path = os.path.join(dest_dir_path, html_file)
            generate_page(dir_path, template_path, dest_path)
        else:
            dest_path = os.path.join(dest_dir_path, file)
            generate_page_recursive(dir_path, template_path, dest_path)
