class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return ' '.join(map(lambda key: f'{key}="{self.props[key]}"', self.props))

    def __repr__(self):
        active_attrs = [];

        if self.tag:
            active_attrs.append(f"tag: {self.tag}")
        if self.value:
            active_attrs.append(f"value: {self.value}")
        if self.children:
            active_attrs.append(f"children: {self.children}")
        if self.props:
            active_attrs.append(f"props: {self.props_to_html()}")

        return f"HTMLNode({', '.join(active_attrs)})"


