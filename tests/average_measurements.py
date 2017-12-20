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
                self.dictionary[self.elements[index]] = index
        else:
            for index in range(len(self.elements)):
                self.dictionary.append(self.elements[index])
        return

    def test_element(self):
        if type(self.dictionary) is dict:
            for element in range(len(self.dictionary)):
                temp = self.dictionary.get(element)
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
                temp = self.dictionary.get(element)
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
                self.dictionary[self.elements[index]] = index
        elif type(self.dictionary) is hash_table.Hash_table:
            for index in range(len(self.elements)):
                self.dictionary.insert(self.dictionary._get_hash(index),
                                       self.elements[index])
        else:
            for index in range(len(self.elements)):
                self.dictionary.insert(index, self.elements[index])
        return

    def test_delete(self):
        try:
            if type(self.dictionary) is dict:
                for element in self.elements:
                    if element in self.dictionary:
                        self.dictionary.pop(element)
            else:
                for element in self.elements:
                    self.dictionary.delete(element)
        except ValueError:
            pass
        return
