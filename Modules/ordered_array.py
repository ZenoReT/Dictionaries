#!/usr/bin/env python3
import sys
import utils


class Ordered_array:
    def __init__(self, elements_type):
        self.ord_array = []
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
        self.ord_array.append(element)
        self.ord_array.sort()

    def element(self, index):
        index = utils.parse_int(index)
        if index is None:
            raise TypeError('Index should be integer!')
        if len(self.ord_array) <= index:
            raise ValueError('Index should be in range of length of array!')
        return self.ord_array[index]

    def index_of(self, element):
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        left_border = 0
        right_border = len(self.ord_array) - 1
        index = int(right_border / 2)
        while self.ord_array[index] != element and left_border < right_border:
            if element > self.ord_array[index]:
                left_border = index + 1
            else:
                right_border = index - 1
            index = int((left_border + right_border) / 2)
        if left_border > right_border or element != self.ord_array[index]:
            return -1
        return index

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
        self.ord_array.remove(element)

    def insert(self, index, element):
        index = utils.parse_int(index)
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        if index is None:
            raise TypeError('Index should be integer!')
        if len(self.ord_array) <= index:
            raise ValueError('Index should be in range of length of array!')
        self.ord_array[index] = element
        self.ord_array.sort()

    def count(self):
        return len(self.ord_array)

    def clear(self):
        self.ord_array = []
