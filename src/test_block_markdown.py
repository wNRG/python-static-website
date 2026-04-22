import unittest

from textnode import TextNode, TextType
from block_markdown import markdown_to_blocks
from blocktype import BlockType, block_to_block_type

class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_block_to_block_type_not_heading(self):
        self.assertEqual(block_to_block_type("####### Too many"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("# Heading\nSecond line"), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```\nsome code here\n```"), BlockType.CODE)

    def test_block_to_block_type_not_code(self):
        self.assertEqual(block_to_block_type("```no newline after backticks```"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("```\nunclosed code"), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> single quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> line one\n> line two"), BlockType.QUOTE)

    def test_block_to_block_type_not_quote(self):
        self.assertEqual(block_to_block_type("> valid\nnot a quote"), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("- item one"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("- item one\n- item two\n- item three"), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_not_unordered_list(self):
        self.assertEqual(block_to_block_type("- valid\nnot an item"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("-no space"), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1. First\n2. Second\n3. Third"), BlockType.ORDERED_LIST)

    def test_block_to_block_type_not_ordered_list(self):
        self.assertEqual(block_to_block_type("2. Starts at two\n3. Third"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1. First\n3. Skips two"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1.No space"), BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph(self):
        self.assertEqual(block_to_block_type("Just a plain paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Multiple lines\nstill a paragraph"), BlockType.PARAGRAPH)
