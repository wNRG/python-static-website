from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    blocks = []
    split_blocks = markdown.split("\n\n")
    
    for block in split_blocks:
        stripped = block.strip()

        if stripped == "":
            continue
        blocks.append(stripped)
    return blocks
    
