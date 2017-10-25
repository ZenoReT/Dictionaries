import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Modules import linear_search
from Modules import ordered_array
from Modules import binary_tree


class FieldTest(unittest.TestCase):
    def test_linear_search_append_all(self):
        linear = linear_search.Linear_search_array("str")
        linear.append("a")
        linear.append("aa")

        expected = ["a", "aa"]

        self.assertEqual(linear.array, expected)

    def test_linear_search_right_element_index(self):
        linear = linear_search.Linear_search_array("str")
        linear.append("a")
        linear.append("aa")
        index = linear.index_of("aa")

        expected = 1

        self.assertEqual(index, expected)

    def test_linear_search_right_element_at_index(self):
        linear = linear_search.Linear_search_array("str")
        linear.append("a")
        linear.append("aa")
        element = linear.element(1)

        expected = "aa"

        self.assertEqual(element, expected)

    def test_ordered_search_append_all(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")

        expected = ["a", "aa"]

        self.assertEqual(ordered.ord_array, expected)

    def test_ordered_search_right_element_index(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")
        index = ordered.index_of("aa")

        expected = 1

        self.assertEqual(index, expected)

    def test_ordered_search_right_element_at_index(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")
        element = ordered.element(1)

        expected = "aa"

        self.assertEqual(element, expected)

    def test_binary_tree_append_all(self):
        tree = binary_tree.Binary_tree("str")
        tree.append("a")
        tree.append("aa")

        expected = ["a", "aa"]

        actually = []
        actually.append(tree.root.value)
        actually.append(tree.root.left.value)

        self.assertEqual(actually, expected)


if __name__ == '__main__':
    unittest.main()
