import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("p", "Lebron James", None, {"href": "https://google.com"})
        self.assertEqual(node.props_to_html(),' href="https://google.com"')

    def test_repr(self):
        node = HTMLNode("p", "Lebron James", None, {"href": "https://google.com"})
        node2 = HTMLNode("p", "Lebron James", None, {"href": "https://google.com"})
        self.assertEqual(repr(node), repr(node2))

    def test_repr2(self):
        node = HTMLNode("p", "Lebron James", None, {"href": "https://google.com"})
        node2 = HTMLNode("a", "Lebron James", None, {"href": "https://google.com"})
        self.assertNotEqual(repr(node), repr(node2))

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
if __name__ == "__main__":
    unittest.main()
