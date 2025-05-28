import re


from textnode import TextNode, TextType
from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL_TEXT :
            return LeafNode(tag= None, value = text_node.text, props=None)
        case TextType.BOLD_TEXT :
            return LeafNode(tag= "b", value = text_node.text, props=None)
        case TextType.ITALIC_TEXT:
            return LeafNode(tag= "i", value = text_node.text, props=None)
        case TextType.CODE_TEXT :
            return LeafNode(tag= "code", value = text_node.text, props=None)
        case TextType.LINK:
            return LeafNode(tag= "a", value = text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
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
    if old_nodes == [] or old_nodes is None:
        return []

    new_nodes = []

    for node in old_nodes:
        temp = extract_markdown_images(node.text)

        word_to_split = node.text
        for item in temp:
            split_result = word_to_split.split(f"![{item[0]}]({item[1]})", 1)
            new_node = TextNode(split_result[0], TextType.NORMAL_TEXT)
            new_nodes.append(new_node)
            del split_result[0]
            new_link_node = TextNode(item[0], TextType.IMAGE, item[1])
            new_nodes.append(new_link_node)
            word_to_split = "".join(split_result)

    return new_nodes



def split_nodes_link(old_nodes):
    if old_nodes == [] or old_nodes is None:
        return []

    new_nodes = []

    for node in old_nodes:
        temp = extract_markdown_links(node.text)

        word_to_split = node.text
        for item in temp:

            split_result = word_to_split.split(f"[{item[0]}]({item[1]})", 1)
            new_node = TextNode(split_result[0], TextType.NORMAL_TEXT)
            new_nodes.append(new_node)
            del split_result[0]
            new_link_node = TextNode(item[0], TextType.LINK,item[1])
            new_nodes.append(new_link_node)
            word_to_split = "".join(split_result)

    return new_nodes


def text_to_textnodes(text):
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    final_result = []
    new_node = TextNode(text, TextType.NORMAL_TEXT)
    extract_bold = split_nodes_delimiter(new_node,"**",TextType.BOLD_TEXT)
    final_result.append(extract_bold[0])
    final_result.append(extract_bold[1])
    del extract_bold[0]
    del extract_bold[0]
    # print(extract_bold)
    extract_italic = split_nodes_delimiter(extract_bold[0], "_", TextType.ITALIC_TEXT)
    final_result.append(extract_italic[0])
    final_result.append(extract_italic[1])
    del extract_italic[0]
    del extract_italic[0]
    extract_code = split_nodes_delimiter(extract_italic[0], "`", TextType.CODE_TEXT)
    final_result.append(extract_code[0])
    final_result.append(extract_code[1])
    del extract_code[0]
    del extract_code[0]
    print(extract_code[0])
    #ISSUE split_nodes_image is not returning the remaining text
    extract_image = split_nodes_image([extract_code[0]])
    print(extract_image)

def main():
    a = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(a)
    text_to_textnodes("")


if __name__ == "__main__":
    main()