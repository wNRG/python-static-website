from htmlnode import HTMLNode, ParentNode, LeafNode 
from textnode import TextNode, TextType, text_node_to_html_node
from block_markdown import markdown_to_blocks
from inline_markdown import text_to_textnodes
from blocktype import BlockType,block_to_block_type 

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(block.replace("\n", " "))
            html_nodes.append(ParentNode("p", children))

        elif block_type == BlockType.HEADING:
            count = heading_counter(block)
            children = text_to_children(block[count:].lstrip())
            html_nodes.append(ParentNode(f"h{count}", children))

        elif block_type == BlockType.QUOTE:
            text = remove_quote_arrow(block)
            children = text_to_children(text)
            html_nodes.append(ParentNode("blockquote", children))
        
        elif block_type == BlockType.UNORDERED_LIST:
            items = unordered_list_items(block)
            children = items_to_li_nodes(items)
            html_nodes.append(ParentNode("ul", children))

        elif block_type == BlockType.ORDERED_LIST:
            items = ordered_list_items(block)
            children = items_to_li_nodes(items)
            html_nodes.append(ParentNode("ol", children))

        elif block_type == BlockType.CODE:
            code_node = strip_code_block(block)
            html_nodes.append(ParentNode("pre", [code_node]))

    return ParentNode("div", html_nodes)

def text_to_children(text):
    children = text_to_textnodes(text)
    html_nodes = []
    for child in children:
        html_nodes.append(text_node_to_html_node(child))
    return html_nodes

def heading_counter(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    return count

def remove_quote_arrow(block):
    cleaned = []
    lines = block.split("\n")

    for line in lines:
        cleaned.append(line.lstrip(">").strip())
    return " ".join(cleaned)

def unordered_list_items(block):
    cleaned = []
    lines = block.split("\n")

    for line in lines:
        cleaned.append(line[2:])
    return cleaned 

def items_to_li_nodes(items):
    li_nodes = []
    for i in items:
        children = text_to_children(i)
        li_nodes.append(ParentNode("li", children))
    return li_nodes
        
def ordered_list_items(block):
    cleaned = []
    lines = block.split("\n")
    count = 0
    for i, line in enumerate(lines, start = 1):
        digits = len(str(i))
        cleaned.append(line[digits + 2:])
    return cleaned

def strip_code_block(block):
    content = block[4:-3]
    child = text_node_to_html_node(TextNode(content, TextType.TEXT))
    return ParentNode("code", [child])


