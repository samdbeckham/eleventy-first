from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent nodes need a tag")
        if self.children == None:
            raise ValueError("Parent nodes need children")
        children = ''.join(list(map(lambda child: child.to_html(), self.children)))
        return f"<{self.tag}>{children}</{self.tag}>"

