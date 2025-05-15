from textnode import TextNode
from texttype import TextType
from extractmarkdownimages import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if node.text_type == TextType.TEXT:
            nodes = split_node(node.text, matches)
            new_nodes.extend(nodes)
        else: 
            new_nodes.append(node)
    return new_nodes

def split_node(str, matches, i = 0):
    if len(matches) < i + 1:
        return [] if len(str) == 0 else [TextNode(str, TextType.TEXT)]
    txt, url = matches[i]
    split_str = str.split(f"![{txt}]({url})")
    text_node = TextNode(split_str[0], TextType.TEXT)
    link_node = TextNode(txt, TextType.IMAGE, url)
    return [text_node, link_node] + split_node(split_str[1], matches, i + 1)
