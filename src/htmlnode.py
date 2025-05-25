

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


class ParentNode(HTMLnode):
    def __init__(self, tag,children, props = None ):
        super().__init__(tag, None ,children, props = props)

    def to_html(self):
        if self.tag is None or self.tag =="":
            raise ValueError("Tag cannot be empty")
        if self.children is None or self.children == "":
            raise ValueError("Children cannot be empty")
        else:
            # return a string representing the HTML tag of the node and its children. This should be a recursive method (each recursion being called on a nested child node).
            html =""
            for child in self.children:
                if type(child) == ParentNode:
                    html = html + child.to_html()
                else:
                    html = html + child.to_html()

            return f"<{self.tag}>{html}</{self.tag}>"

