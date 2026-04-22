import sys
from textnode import TextNode, TextType
from copy_static import copy_static_to_public
from generatepage import generate_page_recursive 

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_template = "./template.html"
dir_path_destination = "./public"
def main():
    test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test)
    copy_static_to_public(dir_path_static, dir_path_public)
    generate_page_recursive(dir_path_content, dir_path_template, dir_path_destination)
if __name__ == "__main__":
    sys.exit(main())

