import unittest

from blocktype import BlockType
from blocktoblocktype import block_to_block_type

class TestBlockToBloxkType(unittest.TestCase):
    def test_heading1(self):
        result = block_to_block_type("# This is a h1")
        self.assertEqual(result, BlockType.HEADING)

    def test_heading6(self):
        result = block_to_block_type("###### This is an h6")
        self.assertEqual(result, BlockType.HEADING)

    def test_heading7(self):
        result = block_to_block_type("####### This is an invalid h7")
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_code(self):
        result = block_to_block_type("```\nprint('hello world')\n```")
        self.assertEqual(result, BlockType.CODE)

    def test_code_too_many(self):
        result = block_to_block_type("````\nprint('goodby everyone')\n````")
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_code_not_enough(self):
        result = block_to_block_type("``\nprint('goodbye')\n``")
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_code_no_closing(self):
        result = block_to_block_type("```\nprint('good')")
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_quote(self):
        result = block_to_block_type("> You can quote me on that")
        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list(self):
        result = block_to_block_type("- eggs\n- milk\n-alan partridge in a pear tree")
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        result = block_to_block_type("1. nothing's wrong with me\n 2. nothing's wrong with me\n 3. nothing's wrong with me\n 4. !!!!!!!")
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_ordered_list_start_2(self):
        result = block_to_block_type("2. I can only count to four.\n3. I can only count to four.\n4. I can only count to")
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_ordered_list_unordered(self):
        result = block_to_block_type("1. Starting strong\n3. Nope, that's not right\n2. 2 little 2 late")
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_paragraph(self):
        result = block_to_block_type("Just a plain old paragraph")
        self.assertEqual(result, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unitest.main()

