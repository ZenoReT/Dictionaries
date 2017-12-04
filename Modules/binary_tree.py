import sys
import utils


class Node:
    def __init__(self, value):
        self.sub_tree_size = 1
        self.value = value
        self.right = None
        self.left = None


class Binary_tree:
    def __init__(self, elements_type):
        (ok, msg) = utils.check_type(elements_type)
        if not ok:
            raise ValueError(msg)
        self.elements_type = msg
        self.root = Node(None)

    def _find_parent_for(self, element):
        current_node = self.root
        previous_node = self.root
        while current_node:
            previous_node = current_node
            current_node.sub_tree_size += 1
            if current_node.value > element:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return previous_node

    def append(self, element):
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        if self.root.value is None:
            self.root.value = element
        else:
            parent_node = self._find_parent_for(element)
            if parent_node.value > element:
                parent_node.left = Node(element)
            else:
                parent_node.right = Node(element)

    def element(self, index):
        index = utils.parse_int(index)
        if index is None:
            raise TypeError('Index should be integer!')
        if self.root is None or self.root.sub_tree_size <= index:
            raise ValueError('Index should be in range of number of elements!')
        current_node = self.root
        while (not(current_node.left is not None and
                   current_node.left.sub_tree_size == index or
                   current_node.left is None and index <= 0)):
            if (current_node.left is not None and
                    current_node.left.sub_tree_size > index):
                current_node = current_node.left
            elif current_node.left is None and current_node.right is not None:
                index -= 1
                current_node = current_node.right
            else:
                index = index - 1 - current_node.left.sub_tree_size
                current_node = current_node.right
        return current_node

    def index_of(self, element):
        index = 0
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        if self.root is None:
            raise ValueError('There are no elements in tree')
        current_node = self.root
        while element != current_node.value:
            if element < current_node.value and current_node.left is not None:
                index = index + 1 + current_node.left.sub_tree_size
                current_node = current_node.left
            elif (element > current_node.value and
                  current_node.right is not None):
                index += 1
                current_node = current_node.right
            else:
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
        current_node = self.root
        parent = current_node
        if current_node is None:
            raise ValueError('The tree is empty')
        while element != current_node.value:
            parent = current_node
            if element < current_node.value and current_node.left is not None:
                current_node = current_node.left
            elif (element > current_node.value and
                  current_node.right is not None):
                current_node = current_node.right
            else:
                raise ValueError('No such element in tree: {0}'
                                 .format(element))
        if current_node.left is None and current_node.right is None:
            if parent.left is not None and parent.left is current_node:
                parent.left = None
            else:
                parent.right = None
        elif current_node.left is not None and current_node.right is None:
            current_node.value = current_node.left.value
            current_node.left = None
        elif current_node.left is None and current_node.right is not None:
            current_node.value = current_node.right.value
            current_node.right = None
        else:
            replace_node = current_node.right
            previous_node = replace_node
            while replace_node.left is not None:
                previous_node = replace_node
                replace_node = replace_node.left
            if replace_node.right is not None:
                previous_node.left = replace_node.right
            current_node.value = replace_node.value

    def insert(self, index, element):
        index = utils.parse_int(index)
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        node = self.root
        previous_node = node
        while node is not None and node.value != element:
            node.sub_tree_size += 1
            previous_node = node
            if node.value < element:
                node = node.left
            elif node.value > element:
                node = node.right
        node = Node(element)
        if element > previous_node.value:
            previous_node.right = node
        else:
            previous_node.left = node

    def count(self):
        if self.root is None:
            return 0
        return self.root.sub_tree_size

    def clear(self):
        self.root = None
