

class HTMLnode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplemented("not yet implemented")

    def props_to_html(self):
        props_string = " "
        if self.props is None:
            return ""

        for item in self.props:
            props_string = props_string + item + "=" + '"'+self.props[item]+ '"' + " "
        return props_string.rstrip()

    def __repr__(self):
        return "Tag: "+self.tag+"\n" + "Value:"+self.value+"\n" + "children:"+ self.children+"\n" + "Properties:"+self.props_to_html()+"\n"


class LeafNode(HTMLnode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag = tag,value = value,props=props)

    def to_html(self):
        if self.value == "" or self.value is None:
            raise ValueError("Value cannot be empty")

        if self.tag is None:
            return str(self.value)
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

