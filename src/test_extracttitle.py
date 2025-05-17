import unittest

from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_oneline(self):
        result = extract_title("# I am the title")
        self.assertEqual(result, "I am the title")

    def test_oneline_miss_h2(self):
        with self.assertRaises(Exception):
            extract_title("## I am the title")

    def test_title_is_buried(self):
        markdown = """
Sometimes we have an opening paragraph to introduce…

# The main title!

Though, I'm not sure if this is legal, I'll allow it.
"""
        result = extract_title(markdown)
        self.assertEqual(result, "The main title!")

    def test_multiple_headings(self):
        markdown = """
# I am the title

Again, this one shouldn't be allowed, but we shouldn't fail for it either.

# No, I am the title!

# There can be only one
"""
        result = extract_title(markdown)
        self.assertEqual(result, "I am the title")

if __name__ == "__main__":
    unitest.main()

