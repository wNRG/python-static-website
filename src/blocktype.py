from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    heading_count = 0
    for char in block:
        if char == "#":
            heading_count += 1
        else:
            break

    if 1 <= heading_count <= 6 and len(block) > heading_count and block[heading_count] == " " and "\n" not in block:
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```") and len(block) > 3 and block[3] == "\n":
        return BlockType.CODE

    lines = block.split("\n")

    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE

    is_unordered = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered = False
            break 
    if is_unordered:
        return BlockType.UNORDERED_LIST

    start = 1
    is_ordered = True
    for line in lines:
        prefix = str(start) + ". "
        if not line.startswith(prefix):
            is_ordered = False
            break
        start += 1
    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


