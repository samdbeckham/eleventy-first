import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr_hello_world(self):
        node = HTMLNode("h1", "Hello World", None, {"class": "heading"})
        self.assertEqual(
            'HTMLNode(tag: h1, value: Hello World, props: class="heading")', repr(node)
        )

    def test_props_to_html(self):
        node = HTMLNode("a", "Example link", None, {"href": "http://example.com", "target": "_blank"})
        self.assertEqual('href="http://example.com" target="_blank"', node.props_to_html())

if __name__ == "__main__":
    unitest.main()

