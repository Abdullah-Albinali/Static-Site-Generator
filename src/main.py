import re


from src.textnode import TextNode, TextType
from src.htmlnode import LeafNode


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

def extract_markdown_images(text):
    return  re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)



def split_nodes_image(old_nodes):
    # if old_nodes.text == "" or old_nodes.text is None:
    #     return []
    #
    # new_nodes = []
    # temp =
    #
    # return new_nodes
    pass



def split_nodes_link(old_nodes):
    if old_nodes.text == "" or old_nodes.text is None:
        return []

    new_nodes = []
    temp = extract_markdown_links(old_nodes.text)
    temp2 = []
    if temp == []:
        return old_nodes
    word_to_split = old_nodes.text
    for item in temp:
        #TODO fix this
        temp2.append(word_to_split.split(f"[{item[0]}]({item[1]})", 1)[0])
        word_to_split = str(word_to_split.split(f"[{item[0]}]({item[1]})", 1)[1:])

    return temp2

def main():
    a = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(a)


if __name__ == "__main__":
    main()