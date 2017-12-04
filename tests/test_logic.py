import unittest
import sys
from modules import linear_search
from modules import ordered_array
from modules import binary_tree
from modules import balanced_tree
from modules import hash_table


class Test_logic(unittest.TestCase):
    def test_linear_append_all(self):
        linear = linear_search.Linear_search("str")
        linear.append("a")
        linear.append("aa")

        expected = ["a", "aa"]

        self.assertEqual(linear.array, expected)

    def test_linear_element_index_works_correct(self):
        linear = linear_search.Linear_search("str")
        linear.append("a")
        linear.append("aa")
        index = linear.index_of("aa")

        expected = 1

        self.assertEqual(index, expected)

    def test_linear_element_at_index_works_correct(self):
        linear = linear_search.Linear_search("str")
        linear.append("a")
        linear.append("aa")
        element = linear.element(1)

        expected = "aa"

        self.assertEqual(element, expected)

    def test_linear_contains_element(self):
        linear = linear_search.Linear_search("str")
        linear.append("a")
        linear.append("aa")

        expected = True
        actually = linear.contains("aa")

        self.assertEqual(expected, actually)

    def test_linear_not_contains_element(self):
        linear = linear_search.Linear_search("str")
        linear.append("a")
        linear.append("aa")

        expected = False
        actually = linear.contains("aaa")

        self.assertEqual(expected, actually)

    def test_linear_not_contains_element_after_deleting(self):
        linear = linear_search.Linear_search("str")
        linear.append("a")
        linear.append("aa")
        linear.delete("aa")

        expected = False
        actually = linear.contains("aa")

        self.assertEqual(expected, actually)

    def test_linear_insert_works_correct(self):
        linear = linear_search.Linear_search("str")
        linear.append("a")
        linear.append("aa")
        linear.insert(1, "aaa")

        expected = "aaa"

        self.assertEqual(expected, linear.element(1))

    def test_linear_count_works_correct(self):
        linear = linear_search.Linear_search("str")
        linear.append("a")
        linear.append("aa")

        expected = 2

        self.assertEqual(expected, linear.count())

    def test_linear_clear_works_correct(self):
        linear = linear_search.Linear_search("str")
        linear.append("a")
        linear.append("aa")
        linear.clear()

        expected = []

        self.assertEqual(expected, linear.array)

    def test_ordered_append_all(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")

        expected = ["a", "aa"]

        self.assertEqual(ordered.ord_array, expected)

    def test_ordered_element_index_works_correct(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")
        index = ordered.index_of("aa")

        expected = 1

        self.assertEqual(index, expected)

    def test_ordered_element_at_index_works_correct(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")
        element = ordered.element(1)

        expected = "aa"

        self.assertEqual(element, expected)

    def test_ordered_contains_element(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")

        expected = True
        actually = ordered.contains("aa")

        self.assertEqual(expected, actually)

    def test_ordered_not_contains_element(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")

        expected = False
        actually = ordered.contains("aaa")

        self.assertEqual(expected, actually)

    def test_ordered_not_contains_element_after_deleting(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")
        ordered.delete("aa")

        expected = False
        actually = ordered.contains("aa")

        self.assertEqual(expected, actually)

    def test_ordered_insert_works_correct(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")
        ordered.insert(1, "aaa")

        expected = "aaa"

        self.assertEqual(expected, ordered.element(1))

    def test_ordered_count_works_correct(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")

        expected = 2

        self.assertEqual(expected, ordered.count())

    def test_ordered_clear_works_correct(self):
        ordered = ordered_array.Ordered_array("str")
        ordered.append("a")
        ordered.append("aa")
        ordered.clear()

        expected = []

        self.assertEqual(expected, ordered.ord_array)

    def test_binary_tree_append_all(self):
        tree = binary_tree.Binary_tree("str")
        tree.append("a")
        tree.append("aa")

        expected = ["a", "aa"]

        actually = []
        actually.append(tree.root.value)
        actually.append(tree.root.right.value)

        self.assertEqual(actually, expected)

    def test_binary_tree_element_index_works_correct(self):
        tree = binary_tree.Binary_tree("str")
        tree.append("a")
        tree.append("aa")

        index = tree.index_of("aa")
        expected = 1

        self.assertEqual(expected, index)

    def test_binary_tree_element_at_index_works_correct(self):
        tree = binary_tree.Binary_tree("str")
        tree.append("a")
        tree.append("aa")
        element = tree.element(1)

        expected = "aa"

        self.assertEqual(element.value, expected)

    def test_binary_tree_contains_element(self):
        tree = binary_tree.Binary_tree("str")
        tree.append("a")
        tree.append("aa")

        expected = True
        actually = tree.contains("aa")

        self.assertEqual(expected, actually)

    def test_binary_tree_not_contains_element(self):
        tree = binary_tree.Binary_tree("str")
        tree.append("a")
        tree.append("aa")

        expected = False
        actually = tree.contains("aaa")

        self.assertEqual(expected, actually)

    def test_binary_tree_not_contains_element_after_deleting(self):
        tree = binary_tree.Binary_tree("str")
        tree.append("a")
        tree.append("aa")
        tree.delete("aa")

        expected = False
        actually = tree.contains("aa")

        self.assertEqual(expected, actually)

    def test_binary_tree_insert_works_correct(self):
        tree = binary_tree.Binary_tree("str")
        tree.append("a")
        tree.append("aa")
        tree.insert(1, "aaa")

        expected = "aaa"
        actually = tree.element(2).value

        self.assertEqual(3, tree.count())
        self.assertEqual(expected, actually)

    def test_binary_tree_count_works_correct(self):
        tree = binary_tree.Binary_tree("str")
        tree.append("a")
        tree.append("aa")

        expected = 2

        self.assertEqual(expected, tree.count())

    def test_binary_tree_clear_works_correct(self):
        tree = binary_tree.Binary_tree("str")
        tree.append("a")
        tree.append("aa")
        tree.clear()

        expected = None
        actually = tree.root

        self.assertEqual(expected, actually)

    def test_balanced_tree_append_all(self):
        tree = balanced_tree.Balanced_tree("str")
        tree.append("a")
        tree.append("aa")

        expected = ["a", "aa"]

        actually = []
        actually.append(tree.root.value)
        actually.append(tree.root.right.value)

        self.assertEqual(actually, expected)

    def test_balanced_tree_element_index_works_correct(self):
        tree = balanced_tree.Balanced_tree("str")
        tree.append("a")
        tree.append("aa")

        index = tree.index_of("aa")
        expected = 1

        self.assertEqual(expected, index)

    def test_balanced_tree_element_at_index_works_correct(self):
        tree = balanced_tree.Balanced_tree("str")
        tree.append("a")
        tree.append("aa")
        element = tree.element(1)

        expected = "aa"

        self.assertEqual(element.value, expected)

    def test_balanced_tree_contains_element(self):
        tree = balanced_tree.Balanced_tree("str")
        tree.append("a")
        tree.append("aa")

        expected = True
        actually = tree.contains("aa")

        self.assertEqual(expected, actually)

    def test_balanced_tree_not_contains_element(self):
        tree = balanced_tree.Balanced_tree("str")
        tree.append("a")
        tree.append("aa")

        expected = False
        actually = tree.contains("aaa")

        self.assertEqual(expected, actually)

    def test_balanced_tree_not_contains_element_after_deleting(self):
        tree = balanced_tree.Balanced_tree("str")
        tree.append("a")
        tree.append("aa")
        tree.delete("aa")

        expected = False
        actually = tree.contains("aa")

        self.assertEqual(expected, actually)

    def test_balanced_tree_insert_works_correct(self):
        tree = balanced_tree.Balanced_tree("str")
        tree.append("a")
        tree.append("aa")
        tree.insert(1, "aaa")

        expected = "aaa"
        actually = tree.element(2).value

        self.assertEqual(3, tree.count())
        self.assertEqual(expected, actually)

    def test_balanced_tree_count_works_correct(self):
        tree = balanced_tree.Balanced_tree("str")
        tree.append("a")
        tree.append("aa")

        expected = 2

        self.assertEqual(expected, tree.count())

    def test_balanced_tree_clear_works_correct(self):
        tree = balanced_tree.Balanced_tree("str")
        tree.append("a")
        tree.append("aa")
        tree.clear()

        expected = None
        actually = tree.root

        self.assertEqual(expected, actually)

    def test_hash_table_append_all(self):
        table = hash_table.Hash_table("str")
        table.append("a")
        table.append("aa")

        expected = ["a", "aa"]
        actually = []

        for key in table.table.keys():
            actually.append(table.table[key])

        self.assertEqual(actually, expected)

    def test_hash_table_element_index(self):
        table = hash_table.Hash_table("str")
        table.append("a")
        table.append("aa")
        index = table.index_of("aa")

        expected = table._get_hash("aa")

        self.assertEqual(index, expected)

    def test_hash_table_element_at_index_works_correct(self):
        table = hash_table.Hash_table("str")
        table.append("a")
        table.append("aa")
        element = table.element(table._get_hash("a"))

        expected = "a"

        self.assertEqual(element, expected)

    def test_hash_table_contains_element(self):
        table = hash_table.Hash_table("str")
        table.append("a")
        table.append("aa")

        expected = True
        actually = table.contains("aa")

        self.assertEqual(expected, actually)

    def test_hash_table_not_contains_element(self):
        table = hash_table.Hash_table("str")
        table.append("a")
        table.append("aa")

        expected = False
        actually = table.contains("aaa")

        self.assertEqual(expected, actually)

    def test_hash_table_not_contains_element_after_deleting(self):
        table = hash_table.Hash_table("str")
        table.append("a")
        table.append("aa")
        table.delete("aa")

        expected = False
        actually = table.contains("aa")

        self.assertEqual(expected, actually)

    def test_hash_table_insert_works_correct(self):
        table = hash_table.Hash_table("str")
        table.append("a")
        table.append("aa")
        table.insert(1, "aaa")

        expected = "aaa"

        self.assertEqual(expected, table.element(1))

    def test_hash_table_count_works_correct(self):
        table = hash_table.Hash_table("str")
        table.append("a")
        table.append("aa")

        expected = 2

        self.assertEqual(expected, table.count())

    def test_hash_table_clear_works_correct(self):
        table = hash_table.Hash_table("str")
        table.append("a")
        table.append("aa")
        table.clear()

        expected = {}

        self.assertEqual(expected, table.table)

if __name__ == '__main__':
    unittest.main()
