#!/usr/bin/env python3
from modules import linear_search
from modules import ordered_array
from modules import binary_tree
from modules import balanced_tree
from modules import hash_table


class Worst_linear_search_measurements:
    def __init__(self, elements):
        self.dictionary = linear_search.Linear_search()
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        temp = self.dictionary.element(len(self.elements) - 1)
        return

    def test_index_of(self):
        temp = self.dictionary.index_of(self.elements[len(self.elements) - 1])
        return

    def test_contains(self):
        temp = self.dictionary.contains(self.elements[len(self.elements) - 1])
        return

    def test_insert(self):
        last_index = len(self.elements) - 1
        self.dictionary.insert(last_index, self.elements[last_index])
        return

    def test_delete(self):
        for index in range(len(self.elements) - 1, -1):
            self.dictionary.delete(self.elements[index])
        return


class Worst_ordered_array_measurements:
    def __init__(self, elements):
        self.dictionary = ordered_array.Ordered_array()
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements) - 1, -1):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        temp = self.dictionary.element(len(self.elements) - 1)
        return

    def test_index_of(self):
        temp = self.dictionary.index_of(self.elements[len(self.elements) // 2])
        return

    def test_contains(self):
        temp = self.dictionary.contains(self.elements[len(self.elements) // 2])
        return

    def test_insert(self):
        last_index = len(self.elements) - 1
        self.dictionary.insert(last_index, self.elements[0])
        return

    def test_delete(self):
        # Was created new min arg after insert and deleted max arg
        self.dictionary.delete(self.elements[0])
        for index in range(len(self.elements) - 1):
            self.dictionary.delete(self.elements[index])


class Worst_binary_tree_measurements:
    def __init__(self, elements):
        self.dictionary = binary_tree.Binary_tree()
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        temp = self.dictionary.element(len(self.elements) - 1)
        return

    def test_index_of(self):
        temp = self.dictionary.index_of(self.elements[len(self.elements) - 1])
        return

    def test_contains(self):
        temp = self.dictionary.contains(self.elements[len(self.elements) - 1])
        return

    def test_insert(self):
        last_index = len(self.elements) - 1
        self.dictionary.insert(last_index, self.elements[last_index])
        return

    def test_delete(self):
        for index in range(len(self.elements) - 1, -1):
            self.dictionary.delete(self.elements[index])


class Worst_balanced_tree_measurements:
    def __init__(self, elements):
        self.dictionary = balanced_tree.Balanced_tree()
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        temp = self.dictionary.element(len(self.elements) - 1)
        return

    def test_index_of(self):
        temp = self.dictionary.index_of(self.elements[len(self.elements) - 1])
        return

    def test_contains(self):
        temp = self.dictionary.contains(self.elements[len(self.elements) - 1])
        return

    def test_insert(self):
        last_index = len(self.elements) - 1
        self.dictionary.insert(last_index, self.elements[last_index])
        return

    def test_delete(self):
        for index in range(len(self.elements) - 1, -1):
            self.dictionary.delete(self.elements[index])


class Worst_hash_table_measurements:
    def __init__(self, elements):
        self.dictionary = hash_table.Hash_table()
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        index = self.dictionary._get_hash(self.elements[0])
        temp = self.dictionary.element(index)
        return

    def test_index_of(self):
        temp = self.dictionary.index_of(self.elements[0])
        return

    def test_contains(self):
        temp = self.dictionary.contains(self.elements[0])
        return

    def test_insert(self):
        last_index = self.dictionary._get_hash(self.elements[0])
        self.dictionary.insert(index, self.elements[0])
        return

    def test_delete(self):
        for index in range(len(self.elements)):
            self.dictionary.delete(self.elements[index])
