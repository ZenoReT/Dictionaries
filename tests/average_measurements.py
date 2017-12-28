#!/usr/bin/env python3
from modules import linear_search
from modules import ordered_array
from modules import binary_tree
from modules import balanced_tree
from modules import hash_table


class Average_measurements:
    def __init__(self, dictionary, elements):
        self.dictionary = dictionary
        self.elements = elements

    def test_append(self):
        if type(self.dictionary) is dict:
            for index in range(len(self.elements)):
                self.dictionary[index] = self.elements[index]
        else:
            for index in range(len(self.elements)):
                self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        if type(self.dictionary) is dict:
            for index in range(len(self.dictionary)):
                temp = self.dictionary.get(index)
        elif type(self.dictionary) is hash_table.Hash_table:
            for index in range(self.dictionary.count()):
                temp = self.dictionary.element(
                    self.dictionary._get_hash(index))
        else:
            for index in range(self.dictionary.count()):
                temp = self.dictionary.element(index)
        return

    def test_index_of(self):
        if type(self.dictionary) is dict:
            for element in self.elements:
                for value in self.dictionary.values():
                    if value == element:
                        temp = element
        else:
            for element in self.elements:
                temp = self.dictionary.index_of(element)
        return

    def test_contains(self):
        if type(self.dictionary) is dict:
            for element in self.elements:
                temp = element in self.dictionary
        else:
            for element in self.elements:
                temp = self.dictionary.contains(element)
        return

    def test_insert(self):
        if type(self.dictionary) is dict:
            for index in range(len(self.elements)):
                self.dictionary[index] = self.elements[index]
        elif type(self.dictionary) is hash_table.Hash_table:
            for index in range(len(self.elements)):
                self.dictionary.insert(self.dictionary._get_hash(index),
                                       self.elements[index])
        elif (type(self.dictionary) is binary_tree.Binary_tree or
              type(self.dictionary) is balanced_tree.Balanced_tree):
            # It's analogue of insert in trees, but don't break connectivity
            for index in range(len(self.elements)):
                temp = self.dictionary.element(index)
                temp.value = temp.value
        else:
            for index in range(len(self.elements)):
                self.dictionary.insert(index, self.elements[index])
        return

    def test_delete(self):
        if type(self.dictionary) is dict:
            try:
                for index in range(len(self.elements)):
                    self.dictionary.pop(index)
            except:
                pass
        elif (type(self.dictionary) is binary_tree.Binary_tree or
                type(self.dictionary) is balanced_tree.Balanced_tree):
            try:
                for index in range(1, len(self.elements)):
                    self.dictionary.delete(self.elements[index])
            except:
                pass
        else:
            try:
                for element in self.elements:
                    self.dictionary.delete(element)
            except:
                pass
        return
