import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        words = old_node.text.split(delimiter)

        if len(words) % 2 == 0:
            raise ValueError("invalid markdown syntax: no closing delimiter found")

        for i, word in enumerate(words):
            if i % 2 == 0:
                new_nodes.append(TextNode(word, TextType.TEXT))
            else:
                new_nodes.append(TextNode(word,text_type))

    return new_nodes

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        remaining_text = old_node.text

        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for alt, url in images:
            sections = remaining_text.split(f"![{alt}]({url})", 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining_text = sections[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        remaining_text = old_node.text

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for alt, link in links:
            sections = remaining_text.split(f"[{alt}]({link})", 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.LINK, link))
            remaining_text = sections[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    images = split_nodes_image(code)
    links = split_nodes_link(images)
    return links
