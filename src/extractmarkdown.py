import re

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            if title:
                return title 
    raise Exception("NO H1 HEADER FOUND")
