import unittest

from markdowntoblocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_multi(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is a list item
- This is another list item
"""
        result = markdown_to_blocks(md)
        self.assertEqual(result, [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is a list item\n- This is another list item" 
        ])

    def test_newline_paragraph(self):
        md = """
This is a paragraph with
text on a new line
"""
        result = markdown_to_blocks(md)
        self.assertEqual(result, ["This is a paragraph with\ntext on a new line"])

    def text_excessive_newlines(self):
        md="""


This text has




way









too many new lines

"""
        result = markdown_to_blocks(md)
        self.assertEqual(result, ["This test has", "way", "too many new lines"])

if __name__ == "__main__":
    unitest.main()

