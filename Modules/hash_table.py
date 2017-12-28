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
        element_hash = self._get_hash(element)
        if element_hash in self.table:
            self.table[element_hash].append(element)
        else:
            self.table[element_hash] = [element]

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
            for i in range(len(self.table[index])):
                if element == self.table[index][i]:
                    return index
        return -1

    def contains(self, element):
        if self.index_of(element) == -1:
            return False
        return True

    def _get_hash(self, element):
        # if you want to break the hash, delete next comment
        # return 1
        current_hash = 0
        const_pow = 1
        element_hash = 0
        element_str = str(element)
        for char in element_str:
            element_hash += ord(char) * (self.const ^ const_pow)
            const_pow += 1
        return element_hash

    def delete(self, element):
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        element_hash = self._get_hash(element)
        if element_hash in self.table:
            for index in range(len(self.table.get(element_hash))):
                if self.table[element_hash][index] == element:
                    self.table[element_hash].pop(index)
                    break
        if len(self.table[element_hash]) == 0:
            self.table.pop(element_hash)

    def insert(self, index, element):
        index = utils.parse_int(index)
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        if index is None:
            raise TypeError('Index should be integer!')
        if index in self.table:
            self.table[index].append(element)
        else:
            self.table[index] = [element]

    def count(self):
        return len(self.table.keys())

    def clear(self):
        self.table = {}
