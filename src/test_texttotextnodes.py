import unittest

from textnode import TextNode
from texttype import TextType
from texttotextnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_one_bold(self):
        result = text_to_textnodes("This text has a **bolded** word in it")
        self.assertEqual(len(result), 3)
        self.assertListEqual(result, [
            TextNode("This text has a ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" word in it", TextType.TEXT),
        ])

    def test_one_italic(self):
        result = text_to_textnodes("This text has an _italicised_ word in it")
        self.assertEqual(len(result), 3)
        self.assertListEqual(result, [
            TextNode("This text has an ", TextType.TEXT),
            TextNode("italicised", TextType.ITALIC),
            TextNode(" word in it", TextType.TEXT),
        ])

    def test_one_code(self):
        result = text_to_textnodes("This text has a `coded` word in it")
        self.assertEqual(len(result), 3)
        self.assertListEqual(result, [
            TextNode("This text has a ", TextType.TEXT),
            TextNode("coded", TextType.CODE),
            TextNode(" word in it", TextType.TEXT),
        ])

    def test_one_image(self):
        result = text_to_textnodes("This text has an ![image](http://placecage.com/666/666) in it")
        self.assertEqual(len(result), 3)
        self.assertListEqual(result, [
            TextNode("This text has an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "http://placecage.com/666/666"),
            TextNode(" in it", TextType.TEXT),
        ])

    def test_one_link(self):
        result = text_to_textnodes("This text has a [link](https://example.com) in it")
        self.assertEqual(len(result), 3)
        self.assertListEqual(result, [
            TextNode("This text has a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" in it", TextType.TEXT),
        ])

    def test_starting_link(self):
        result = text_to_textnodes("[A link](#) right at the start")
        self.assertEqual(len(result), 2)
        self.assertListEqual(result, [
            TextNode("A link", TextType.LINK, "#"),
            TextNode(" right at the start", TextType.TEXT)
        ])

    def test_all(self):
        result = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(len(result), 10)
        self.assertListEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

if __name__ == "__main__":
    unitest.main()

