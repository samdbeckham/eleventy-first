import unittest

from textnode import TextNode
from texttype import TextType
from splitnodeslink import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(len(result), 2)
        self.assertListEqual(result, [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        ])

    def test_link_with_trail(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and no more"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(len(result), 3)
        self.assertListEqual(result, [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and no more", TextType.TEXT)
        ])

    def test_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(len(result), 4)
        self.assertListEqual(result, [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ])

    def test_starting_link(self):
        text = "[A link](#) right at the start"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(len(result), 2)
        self.assertListEqual(result, [
            TextNode("A link", TextType.LINK, "#"),
            TextNode(" right at the start", TextType.TEXT)
        ])

    def test_no_links(self):
        text = "This is text with no links"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(len(result), 1)
        self.assertListEqual(result, [
            TextNode("This is text with no links", TextType.TEXT),
        ])

    def test_italic_passthrough(self):
        text_node1 = TextNode("This text has an ", TextType.TEXT)
        italic_node = TextNode("italic", TextType.ITALIC)
        text_node2 = TextNode(" word and a [link](https://example.com)", TextType.TEXT)
        result = split_nodes_link([text_node1, italic_node, text_node2])
        self.assertEqual(len(result), 4)
        self.assertListEqual(result, [
            text_node1,
            italic_node,
            TextNode(" word and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
        ])

if __name__ == "__main__":
    unitest.main()

