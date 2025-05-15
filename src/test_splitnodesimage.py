import unittest

from textnode import TextNode, TextType
from splitnodesimage import split_nodes_image

class TestSplitNodesLink(unittest.TestCase):
    def test_image(self):
        text = "This is text with an image ![to boot dev](https://www.boot.dev)"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(len(result), 2)
        self.assertListEqual(result, [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev")
        ])

    def test_image_with_trail(self):
        text = "This is text with an image ![to boot dev](https://www.boot.dev) and no more"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(len(result), 3)
        self.assertListEqual(result, [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and no more", TextType.TEXT)
        ])

    def test_images(self):
        text = "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(len(result), 4)
        self.assertListEqual(result, [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")
        ])

    def test_no_links(self):
        text = "This is text with no links"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(len(result), 1)
        self.assertListEqual(result, [
            TextNode("This is text with no links", TextType.TEXT),
        ])

if __name__ == "__main__":
    unitest.main()

