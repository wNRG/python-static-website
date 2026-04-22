import unittest

from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode 
from textnode import TextNode, TextType, text_node_to_html_node
from block_markdown import markdown_to_blocks
from inline_markdown import text_to_textnodes
from blocktype import BlockType,block_to_block_type 

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
# Heading 1

## Heading 2

### Heading 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
        )

    def test_heading_with_inline(self):
        md = """
## This is **bold** heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>This is <b>bold</b> heading</h2></div>",
        )

    def test_quote(self):
        md = """
> This is a quote
> with multiple lines
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with multiple lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- item one
- item two
- item three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>item one</li><li>item two</li><li>item three</li></ul></div>",
        )

    def test_unordered_list_with_inline(self):
        md = """
- item with **bold**
- item with _italic_
- item with `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>item with <b>bold</b></li><li>item with <i>italic</i></li><li>item with <code>code</code></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. first item
2. second item
3. third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first item</li><li>second item</li><li>third item</li></ol></div>",
        )

    def test_ordered_list_with_inline(self):
        md = """
1. item with **bold**
2. item with _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>item with <b>bold</b></li><li>item with <i>italic</i></li></ol></div>",
        )

    def test_mixed_blocks(self):
        md = """
# My Title

This is a paragraph with **bold** text.

- list item one
- list item two
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>My Title</h1><p>This is a paragraph with <b>bold</b> text.</p><ul><li>list item one</li><li>list item two</li></ul></div>",
        )
