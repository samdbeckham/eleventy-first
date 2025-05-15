from enum import Enum

class BlockType(Enum):
    CODE = "CODE"
    PARAGRAPH = "PARAGRAPH"
    HEADING = "HEADING"
    QUOTE = "QUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST = "ORDERED_LIST"
