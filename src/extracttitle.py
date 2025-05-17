import re

def extract_title(markdown):
    match = re.search("^# (.*)$", markdown, re.MULTILINE)
    if not match:
        raise Exception("Title not found")

    return match.group(1)

