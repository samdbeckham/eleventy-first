import unittest

from markdowntohtmlnode import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
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
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_single_line_paragraph(self):
        markdown = "Hello, world!"
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        self.assertEqual(result, "<div><p>Hello, world!</p></div>")

    def test_heading_1(self):
        markdown = "# Hello, world!"
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        self.assertEqual(result, "<div><h1>Hello, world!</h1></div>")

    def test_heading_3(self):
        markdown = "### Hello, world!"
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        self.assertEqual(result, "<div><h3>Hello, world!</h3></div>")

    def test_blockquote(self):
        markdown = "> This is a quote with **bold** text!"
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        self.assertEqual(result, "<div><blockquote>This is a quote with <b>bold</b> text!</blockquote></div>")

    def test_unordered_list(self):
        markdown = """
- list
- of items
- with **bold** text
- and [links](http://example.com)
"""
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        self.assertEqual(result, '<div><ul><li>list</li><li>of items</li><li>with <b>bold</b> text</li><li>and <a href="http://example.com">links</a></li></ul></div>')

    def test_ordered_list(self):
        markdown = """
1. list
2. of items
3. with **bold** text
4. and [links](http://example.com)
"""
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        self.assertEqual(result, '<div><ol><li>list</li><li>of items</li><li>with <b>bold</b> text</li><li>and <a href="http://example.com">links</a></li></ol></div>')

if __name__ == "__main__":
    unitest.main()

