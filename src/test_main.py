import unittest

from main import text_node_to_html_node, split_nodes_delimiter,extract_markdown_images,extract_markdown_links, split_nodes_link, split_nodes_image
from textnode import TextNode,TextType

class Testmain(unittest.TestCase):
    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        after_split = split_nodes_delimiter(node,"`",TextType.CODE_TEXT)
        self.assertEqual(after_split,  [
        TextNode("This is text with a ", TextType.NORMAL_TEXT),
        TextNode("code block", TextType.CODE_TEXT),
        TextNode(" word", TextType.NORMAL_TEXT),
        ])

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.NORMAL_TEXT)
        after_split = split_nodes_delimiter(node,"_",TextType.ITALIC_TEXT)
        self.assertEqual(after_split,  [
        TextNode("This is text with a ", TextType.NORMAL_TEXT),
        TextNode("italic block", TextType.ITALIC_TEXT),
        TextNode(" word", TextType.NORMAL_TEXT),
        ])

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.NORMAL_TEXT)
        after_split = split_nodes_delimiter(node,"**",TextType.BOLD_TEXT)
        self.assertEqual(after_split,  [
        TextNode("This is text with a ", TextType.NORMAL_TEXT),
        TextNode("bold block", TextType.BOLD_TEXT),
        TextNode(" word", TextType.NORMAL_TEXT),
        ])



    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        print(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.NORMAL_TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

