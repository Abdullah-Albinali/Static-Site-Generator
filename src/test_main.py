import unittest

from main import text_node_to_html_node, split_nodes_delimiter
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



