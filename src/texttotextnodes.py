from textnode import TextNode
from texttype import TextType
from splitnodesdelimiter import split_nodes_delimiter
from splitnodesimage import split_nodes_image
from splitnodeslink import split_nodes_link

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return list(filter(lambda node: node.text != "", nodes))
