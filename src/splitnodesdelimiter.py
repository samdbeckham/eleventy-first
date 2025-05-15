from textnode import TextNode
from texttype import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = [];
    for node in old_nodes:
        chunks = node.text.split(delimiter);
        if len(chunks) == 1 or node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif len(chunks) % 2 == 0:
            # There has to be an odd number of nodes, probably
            raise Exception("invalid markdown syntax")
        else:
            for i in range(0, len(chunks)):
                node_text_type = TextType.TEXT if i % 2 == 0 else text_type
                if len(chunks[i]) > 0:
                    new_nodes.append(TextNode(chunks[i], node_text_type))
    return new_nodes
