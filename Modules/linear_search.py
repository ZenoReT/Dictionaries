#!/usr/bin/env python3
import sys
import utils


class Linear_search:
    def __init__(self, elements_type):
        self.array = []
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
        self.array.append(element)

    def element(self, index):
        index = utils.parse_int(index)
        if index is None:
            raise TypeError('Index should be integer!')
        if len(self.array) <= index:
            raise ValueError('Index should be in range of length of array!')
        return self.array[index]

    def index_of(self, element):
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        for i in range(len(self.array)):
            if self.array[i] == element:
                return i
        return -1

    def contains(self, element):
        if self.index_of(element) == -1:
            return False
        return True

    def delete(self, element):
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        self.array.remove(element)

    def insert(self, index, element):
        index = utils.parse_int(index)
        value = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        if index is None:
            raise TypeError('Index should be integer!')
        if len(self.array) <= index:
            raise ValueError('Index should be in range of length of array!')
        self.array[index] = element

    def count(self):
        return len(self.array)

    def clear(self):
        self.array = []
