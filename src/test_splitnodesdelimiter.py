import unittest

from textnode import TextNode
from texttype import TextType
from splitnodesdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is a text node with **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_double_code(self):
        node = TextNode("This has `one` bit of code and `another` bit too", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text_type, TextType.CODE)
        self.assertEqual(result[4].text_type, TextType.TEXT)

    def test_bold_and_italics(self):
        bold_node = TextNode("This is a text node with **bold** text", TextType.TEXT)
        italic_node = TextNode("This is a text node with _italic_ text", TextType.TEXT)
        bold_node2 = TextNode("This is a text node with **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([bold_node, italic_node, bold_node2], "**", TextType.BOLD)
        self.assertEqual(len(result), 7)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text_type, TextType.TEXT)
        self.assertEqual(result[4].text_type, TextType.TEXT)
        self.assertEqual(result[5].text_type, TextType.BOLD)
        self.assertEqual(result[6].text_type, TextType.TEXT)

    def test_no_closing(self):
        node = TextNode("This node traif off before it is **finished", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_opening_with_italics(self):
        node = TextNode("_This_ starts with italic text", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text_type, TextType.ITALIC)
        self.assertEqual(result[1].text_type, TextType.TEXT)

    def text_closing_with_code(self):
        node = TextNode("This closes with `code`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.CODE)

    def test_delimiters_in_code_blocks(self):
        node = TextNode("This is a **code**block", TextType.CODE)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [node])

if __name__ == "__main__":
    unitest.main()

