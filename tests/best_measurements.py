#!/usr/bin/env python3
from modules import linear_search
from modules import ordered_array
from modules import binary_tree
from modules import balanced_tree
from modules import hash_table


class Best_linear_search_measurements:
    def __init__(self, elements):
        self.dictionary = linear_search.Linear_search('int')
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        temp = self.dictionary.element(0)
        return

    def test_index_of(self):
        temp = self.dictionary.index_of(self.elements[0])
        return

    def test_contains(self):
        temp = self.dictionary.contains(self.elements[0])
        return

    def test_insert(self):
        self.dictionary.insert(0, self.elements[0])
        return

    def test_delete(self):
        for index in range(len(self.elements)):
            self.dictionary.delete(self.elements[index])
        return


class Best_ordered_array_measurements:
    def __init__(self, elements):
        self.dictionary = ordered_array.Ordered_array('int')
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        temp = self.dictionary.element(0)
        return

    def test_index_of(self):
        temp = self.dictionary.index_of(self.elements[0])
        return

    def test_contains(self):
        temp = self.dictionary.contains(self.elements[0])
        return

    def test_insert(self):
        self.dictionary.insert(0, self.elements[0])
        return

    def test_delete(self):
        for index in range(len(self.elements)):
            self.dictionary.delete(self.elements[index])


class Best_binary_tree_measurements:
    def __init__(self, elements):
        self.dictionary = binary_tree.Binary_tree('int')
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        temp = self.dictionary.element(0)
        return

    def test_index_of(self):
        temp = self.dictionary.index_of(self.elements[0])
        return

    def test_contains(self):
        temp = self.dictionary.contains(self.elements[0])
        return

    def test_insert(self):
        self.dictionary.insert(0, self.elements[0])
        return

    def test_delete(self):
        for index in range(len(self.elements)):
            self.dictionary.delete(self.elements[index])


class Best_balanced_tree_measurements:
    def __init__(self, elements):
        self.dictionary = balanced_tree.Balanced_tree('int')
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        temp = self.dictionary.element(0)
        return

    def test_index_of(self):
        temp = self.dictionary.index_of(self.elements[0])
        return

    def test_contains(self):
        temp = self.dictionary.contains(self.elements[0])
        return

    def test_insert(self):
        self.dictionary.insert(0, self.elements[0])
        return

    def test_delete(self):
        for index in range(len(self.elements)):
            self.dictionary.delete(self.elements[index])


class Best_hash_table_measurements:
    def __init__(self, elements):
        self.dictionary = hash_table.Hash_table('int')
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
        self.dictionary.insert(last_index, self.elements[0])
        return

    def test_delete(self):
        for index in range(len(self.elements)):
            try:
                self.dictionary.delete(self.elements[index])
            except KeyError:
                pass


class Best_dict_measurements:
    def __init__(self, elements):
        self.dictionary = {}
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary[self.elements[index]] = index
        return

    def test_element(self):
        first_index = 0
        for index in self.dictionary.values():
            if first_index == index:
                temp = index
                break
        return

    def test_index_of(self):
        temp = self.dictionary[1]
        return

    def test_contains(self):
        temp = self.elements[0] in self.dictionary
        return

    def test_insert(self):
        self.dictionary[self.elements[0]] = 0
        return

    def test_delete(self):
        for element in self.elements:
            try:
                self.dictionary.pop(element)
            except KeyError:
                pass
