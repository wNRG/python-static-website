import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links
from extractmarkdown import extract_title

class TestExtractMarkdown(unittest.TestCase):

    def test_extract_markdown_images_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        x = extract_markdown_images(text)
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(x, expected_result)

    def test_extract_makdown_links_1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        x = extract_markdown_links(text)
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(x, expected_result)

    def test_extract_title(self):
        markdown = "# Lebron James "
        x = extract_title(markdown)
        self.assertEqual(x, "Lebron James")

    def test_indented_h1(self):
        self.assertEqual(extract_title("   # Indented Title"), "Indented Title")

    def test_no_header(self):
        with self.assertRaises(Exception):
            extract_title("Just text here")

    def test_h2_not_allowed(self):
        with self.assertRaises(Exception):
            extract_title("## Subtitle")

    def test_empty_title(self):
        with self.assertRaises(Exception):
            extract_title("#   ")
