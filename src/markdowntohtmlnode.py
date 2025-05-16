import re
from blocktoblocktype import block_to_block_type
from blocktype import BlockType
from leafnode import LeafNode
from markdowntoblocks import markdown_to_blocks
from parentnode import ParentNode
from textnodetohtmlnode import text_node_to_html_node
from texttotextnodes import text_to_textnodes

def text_to_children(text):
    return list(map(text_node_to_html_node, text_to_textnodes(text)))

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = [];

    for block in blocks:
        block_type = block_to_block_type(block)
        match(block_type):
            case BlockType.PARAGRAPH:
                text = block.replace("\n", " ")
                text_nodes = text_to_children(text)
                nodes.append(ParentNode('p', text_nodes))
            case BlockType.HEADING:
                pounds, text = block.split(' ', 1)
                nodes.append(LeafNode(f"h{len(pounds)}", text))
            case BlockType.CODE:
                code_block = LeafNode('code', block.removeprefix("```").removesuffix("```").strip())
                nodes.append(ParentNode('pre', [code_block]))
            case BlockType.QUOTE:
                text = block.removeprefix("> ")
                text_nodes = text_to_children(text)
                nodes.append(ParentNode("blockquote", text_nodes))
            case BlockType.UNORDERED_LIST:
                list_items = block.removeprefix('- ').split('\n- ')
                item_nodes = []
                for item in list_items:
                    text_nodes = text_to_children(item)
                    item_nodes.append(ParentNode("li", text_nodes))
                nodes.append(ParentNode('ul', item_nodes))
            case BlockType.ORDERED_LIST:
                list_items = re.split(r'\n\d\. ', block.removeprefix('1. '))
                item_nodes = []
                for item in list_items:
                    text_nodes = text_to_children(item)
                    item_nodes.append(ParentNode("li", text_nodes))
                nodes.append(ParentNode('ol', item_nodes))
            case _:
                raise Exception("invalid block type")

    return ParentNode('div', nodes)

