import sys
from textnode import TextNode, TextType
from copy_static import copy_static_to_public
from generatepage import generate_page_recursive 

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
dir_path_template = "./template.html"
dir_path_destination = "./docs"

def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"

    copy_static_to_public(dir_path_static, dir_path_public)
    generate_page_recursive(dir_path_content, dir_path_template, dir_path_destination, base_path)
if __name__ == "__main__":
    sys.exit(main())

