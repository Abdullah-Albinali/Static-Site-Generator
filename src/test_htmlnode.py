import unittest

from htmlnode import HTMLnode,LeafNode


class TestHTMLNode(unittest.TestCase):
    def test1(self):
        test = HTMLnode("a", "b", "c", {"href": "https://www.google.com", "target": "_blank", })
        self.assertEqual(test.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test2(self):
        test = HTMLnode("a", "b", "c", {"href": "https://www.google.com", "target": "_blank", })
        self.assertEqual(str(test), 'Tag: a\nValue:b\nchildren:c\nProperties: href="https://www.google.com" target="_blank"\n')


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')



if __name__ == '__main__':
    unittest.main()
