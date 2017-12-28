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
        for index in range(len(self.elements)):
            temp = self.dictionary.element(0)
        return

    def test_index_of(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.index_of(self.elements[0])
        return

    def test_contains(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.contains(self.elements[0])
        return

    def test_insert(self):
        for index in range(len(self.elements)):
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
        for index in range(len(self.elements)):
            temp = self.dictionary.element(0)
        return

    def test_index_of(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.index_of(self.elements[0])
        return

    def test_contains(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.contains(self.elements[0])
        return

    def test_insert(self):
        for index in range(len(self.elements)):
            self.dictionary.insert(0, self.elements[0])
        return

    def test_delete(self):
        for index in range(len(self.elements)):
            self.dictionary.delete(self.elements[index])
        return


class Best_binary_tree_measurements:
    def __init__(self, elements):
        self.dictionary = binary_tree.Binary_tree('int')
        self.elements = elements

    def test_append(self):
        self.dictionary.append(self.elements[len(self.elements) // 2])
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.element(0)
        return

    def test_index_of(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.index_of(self.elements[0])
        return

    def test_contains(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.contains(self.elements[0])
        return

    def test_insert(self):
        for index in range(len(self.elements)):
            self.dictionary.insert(1, self.elements[0])
        return

    def test_delete(self):
        for index in range(len(self.elements)):
            try:
                self.dictionary.delete(self.elements[index])
            except:
                pass
        return


class Best_balanced_tree_measurements:
    def __init__(self, elements):
        self.dictionary = balanced_tree.Balanced_tree('int')
        self.elements = elements

    def test_append(self):
        self.dictionary.append(self.elements[len(self.elements) // 2])
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.element(0)
        return

    def test_index_of(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.index_of(self.elements[0])
        return

    def test_contains(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.contains(self.elements[0])
        return

    def test_insert(self):
        for index in range(len(self.elements)):
            self.dictionary.insert(1, self.elements[0])

    def test_delete(self):
        for index in range(len(self.elements)):
            try:
                self.dictionary.delete(self.elements[index])
            except:
                pass
        return


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
        for i in range(len(self.elements)):
            temp = self.dictionary.element(index)
        return

    def test_index_of(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.index_of(self.elements[0])
        return

    def test_contains(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.contains(self.elements[0])
        return

    def test_insert(self):
        last_index = self.dictionary._get_hash(self.elements[0])
        for index in range(len(self.elements)):
            self.dictionary.insert(last_index, self.elements[0])
        return

    def test_delete(self):
        try:
            for element in self.elements:
                self.dictionary.delete(element)
        except:
            pass
        return


class Best_dict_measurements:
    def __init__(self, elements):
        self.dictionary = {}
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary[index] = self.elements[index]
        return

    def test_element(self):
        for index in range(len(self.elements)):
            temp = self.dictionary[1]
        return

    def test_index_of(self):
        first_element = self.elements[0]
        for index in range(len(self.elements)):
            for element in self.dictionary.values():
                if element == first_element:
                    temp = element
                    break
        return

    def test_contains(self):
        for index in range(len(self.elements)):
            temp = self.elements[0] in self.dictionary
        return

    def test_insert(self):
        for index in range(len(self.elements)):
            self.dictionary[self.elements[0]] = 0
        return

    def test_delete(self):
        for index in range(len(self.elements)):
            try:
                self.dictionary.pop(self.elements[index])
            except:
                pass
        return
