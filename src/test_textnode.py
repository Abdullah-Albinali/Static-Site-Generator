import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node",TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node",TextType.BOLD_TEXT)
        self.assertEqual(node,node2)

    def test_eq_url_none(self):
        node = TextNode("This is a text node",TextType.BOLD_TEXT,None)
        node2 = TextNode("This is a text node",TextType.BOLD_TEXT,None)
        self.assertEqual(node,node2)
    def test_eq_normal(self):
        node = TextNode("This is a text node",TextType.NORMAL_TEXT)
        node2 = TextNode("This is a text node",TextType.NORMAL_TEXT)
        self.assertEqual(node,node2)
    def test_eq_image(self):
        node = TextNode("This is a text node",TextType.IMAGE)
        node2 = TextNode("This is a text node",TextType.IMAGE)
        self.assertEqual(node,node2)
    def test_not_eq_image(self):
        node = TextNode("This is a text node",TextType.LINK)
        node2 = TextNode("This is a text node",TextType.IMAGE)
        self.assertNotEqual(node,node2)


if __name__ == '__main__':
    unittest.main()
