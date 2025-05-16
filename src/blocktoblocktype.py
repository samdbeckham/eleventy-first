import re
from blocktype import BlockType

def block_to_block_type(block):
    if re.search("^#{1,6} ", block):
        return BlockType.HEADING
    if re.search("^```\n.*\n```$", block, re.DOTALL):
        return BlockType.CODE
    if re.search("^>", block):
        return BlockType.QUOTE
    if re.search("^- ", block):
        return BlockType.UNORDERED_LIST
    if re.search("^1\. ", block):
        numbers = re.findall("\\n(\d+)\. ", block)
        if sorted(numbers) == numbers:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
