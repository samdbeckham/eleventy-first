def strip_empty_nodes(nodes):
    return list(filter(lambda node: node.text != "", nodes))
