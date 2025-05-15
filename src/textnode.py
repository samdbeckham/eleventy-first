from texttype import TextType

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and self.text_type.value == other.text_type.value and self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


