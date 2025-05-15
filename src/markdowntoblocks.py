def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = list(map(lambda block: block.strip(), blocks))
    return stripped_blocks
