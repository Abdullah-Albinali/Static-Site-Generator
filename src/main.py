from unittest import case

from textnode import TextNode, TextType
from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case(TextType.NORMAL_TEXT):
            return LeafNode(tag= None, value = text_node.text, props=None)
        case(TextType.BOLD_TEXT):
            return LeafNode(tag= "b", value = text_node.text, props=None)
        case(TextType.ITALIC_TEXT):
            return LeafNode(tag= "i", value = text_node.text, props=None)
        case(TextType.CODE_TEXT):
            return LeafNode(tag= "code", value = text_node.text, props=None)
        case (TextType.LINK):
            return LeafNode(tag= "a", value = text_node.text, props={"href": text_node.url})
        case (TextType.IMAGE):
            return LeafNode(tag= "img", value = "", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid text node type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes.text == "" or old_nodes.text is None:
        return []

    new_nodes = []

    temp = old_nodes.text.split(delimiter)
    for index, item in enumerate(temp):
        if index in (0,len(temp)-1):
            new_nodes.append(TextNode(item, TextType.NORMAL_TEXT))
        else:
            new_nodes.append(TextNode(item, text_type))
    return new_nodes



# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# [
#     TextNode("This is text with a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" word", TextType.TEXT),
# ]



def main():
    a = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(a)


if __name__ == "__main__":
    main()