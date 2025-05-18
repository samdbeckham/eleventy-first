import unittest

from extractmarkdownlinks import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_starting_link(self):
        text = "[A link](#) right at the start"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("A link", "#")])

    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unitest.main()

