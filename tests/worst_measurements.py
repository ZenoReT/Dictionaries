#!/usr/bin/env python3
from modules import linear_search
from modules import ordered_array
from modules import binary_tree
from modules import balanced_tree
from modules import hash_table


class Worst_linear_search_measurements:
    def __init__(self, elements):
        self.dictionary = linear_search.Linear_search('int')
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.element(len(self.elements) - 1)
        return

    def test_index_of(self):
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            temp = self.dictionary.index_of(self.elements[last_index])
        return

    def test_contains(self):
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            temp = self.dictionary.contains(self.elements[last_index])
        return

    def test_insert(self):
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            self.dictionary.insert(last_index, self.elements[last_index])
        return

    def test_delete(self):
        for index in range(len(self.elements) - 1, -1, -1):
            self.dictionary.delete(self.elements[index])
        return


class Worst_ordered_array_measurements:
    def __init__(self, elements):
        self.dictionary = ordered_array.Ordered_array('int')
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements) - 1, -1, -1):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.element(len(self.elements) - 1)
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
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            self.dictionary.insert(last_index - index, self.elements[index])
        return

    def test_delete(self):
        cur_len = self.dictionary.count()
        while cur_len != 0:
            self.dictionary.delete(self.dictionary.element(cur_len // 2))
            cur_len = self.dictionary.count()
        return


class Worst_binary_tree_measurements:
    def __init__(self, elements):
        self.dictionary = binary_tree.Binary_tree('int')
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.element(len(self.elements) - 1)
        return

    def test_index_of(self):
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            temp = self.dictionary.index_of(self.elements[last_index])
        return

    def test_contains(self):
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            temp = self.dictionary.contains(self.elements[last_index])
        return

    def test_insert(self):
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            self.dictionary.insert(last_index - 1, self.elements[last_index])
        return

    def test_delete(self):
        for index in range(len(self.elements) - 1, -1, -1):
            try:
                self.dictionary.delete(self.elements[index])
            except:
                pass
        return


class Worst_balanced_tree_measurements:
    def __init__(self, elements):
        self.dictionary = balanced_tree.Balanced_tree('int')
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.element(len(self.elements) - 1)
        return

    def test_index_of(self):
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            temp = self.dictionary.index_of(self.elements[last_index])
        return

    def test_contains(self):
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            temp = self.dictionary.contains(self.elements[last_index])
        return

    def test_insert(self):
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            self.dictionary.insert(last_index - 1, self.elements[last_index])
        return

    def test_delete(self):
        for index in range(len(self.elements) - 1, -1, -1):
            try:
                self.dictionary.delete(self.elements[index])
            except:
                pass
        return


class Worst_hash_table_measurements:
    def __init__(self, elements):
        self.dictionary = hash_table.Hash_table('int')
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        last_index = len(self.elements) - 1
        index = self.dictionary._get_hash(self.elements[last_index])
        for i in range(len(self.elements)):
            temp = self.dictionary.element(index)
        return

    def test_index_of(self):
        last_index = len(self.elements) - 1
        for index in range(len(self.elements)):
            temp = self.dictionary.index_of(self.elements[last_index])
        return

    def test_contains(self):
        last_index = len(self.elements)-1
        for index in range(len(self.elements)):
            temp = self.dictionary.contains(self.elements[last_index])
        return

    def test_insert(self):
        for index in range(len(self.elements)):
            self.dictionary.insert(0, self.elements[0])
        return

    def test_delete(self):
        try:
            for index in range(len(self.elements)-1, -1, -1):
                self.dictionary.delete(self.elements[index])
        except:
            pass
        return


class Worst_dict_measurements:
    def __init__(self, elements):
        self.dictionary = {}
        self.elements = elements

    def test_append(self):
        for index in range(len(self.elements)):
            self.dictionary[index] = self.elements[index]
        return

    def test_element(self):
        for index in range(len(self.elements)):
            temp = self.dictionary.get(0)
        return

    def test_index_of(self):
        last_element = self.elements[len(self.elements) - 1]
        for index in range(len(self.elements)):
            for element in self.dictionary.values():
                if element == last_element:
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
        for index in range(len(self.elements)-1, -1, -1):
            try:
                self.dictionary.pop(self.elements[index])
            except:
                pass
        return
