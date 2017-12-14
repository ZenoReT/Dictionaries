#!/usr/bin/env python3
import sys
import utils


class Hash_table:
    def __init__(self, elements_type):
        self.table = {}
        # const - some of primary number for generating hash.
        self.const = 991
        (ok, msg) = utils.check_type(elements_type)
        if not ok:
            raise ValueError(msg)
        self.elements_type = msg

    def append(self, element):
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        self.table[self._get_hash(element)] = element

    def element(self, index):
        index = utils.parse_int(index)
        if index is None:
            raise TypeError('Index should be integer!')
        if index in self.table:
            return self.table[index]

    def index_of(self, element):
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        index = self._get_hash(element)
        if index in self.table:
            return index
        return -1

    def contains(self, element):
        if self.index_of(element) == -1:
            return False
        return True

    def _get_hash(self, element):
        element_hash = 0
        element_str = str(element)
        for char in element_str:
            temp = element_hash * self.const + ord(char)
            element_hash += (temp % len(element_str))
        return element_hash

    def delete(self, element):
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        self.table.pop(self._get_hash(element))

    def insert(self, index, element):
        index = utils.parse_int(index)
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        if index is None:
            raise TypeError('Index should be integer!')
        self.table[index] = element

    def count(self):
        return len(self.table.keys())

    def clear(self):
        self.table = {}
