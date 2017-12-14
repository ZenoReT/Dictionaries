#!/usr/bin/env python3
import sys
import utils


class Node:
    def __init__(self, value, parent):
        self.sub_tree_size = 1
        self.value = value
        self.right = None
        self.left = None
        self.parent = parent
        self.balance_factor = 0


class Balanced_tree:
    def __init__(self, elements_type):
        (ok, msg) = utils.check_type(elements_type)
        if not ok:
            raise ValueError(msg)
        self.elements_type = msg
        self.root = Node(None, None)

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

    def _rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = root
        new_root.parent = root.parent
        if root.parent is None:
            self.root = new_root
        else:
            if root.parent.right == root:
                root.parent.right = new_root
            else:
                root.parent.left = new_root
        new_root.right = root
        root.parent = new_root
        root.balance_factor += 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor += 1 + max(root.balance_factor, 0)

    def _rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = root
        new_root.parent = root.parent
        if root.parent is None:
            self.root = new_root
        else:
            if root.parent.left == root:
                root.parent.left = new_root
            else:
                root.parent.right = new_root
        new_root.left = root
        root.parent = new_root
        root.balance_factor += 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor += 1 + max(root.balance_factor, 0)

    def _update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self._rebalance(node)
        if node.parent is not None:
            if node.left is not None:
                node.parent.balance_factor += 1
            elif node.right is not None:
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self._update_balance(node.parent)

    def _rebalance(self, node):
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                self._rotate_right(node.right)
                self._rotate_left(node)
            else:
                self._rotate_left(node)
        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                self._rotate_left(node.left)
                self._rotate_right(node)
            else:
                self._rotate_right(node)

    def append(self, element):
        element = utils.try_lead_to(element, self.elements_type)
        if element is None:
            raise TypeError('Unacceptable type of element: {0}\n\
                             \rShould be: {1}'.format(type(element),
                                                      self.elements_type))
        if self.root.value is None:
            self.root = Node(element, None)
        else:
            parent_node = self._find_parent_for(element)
            if parent_node.value > element:
                parent_node.left = Node(element, parent_node)
                self._update_balance(parent_node.left)
            else:
                parent_node.right = Node(element, parent_node)
                self._update_balance(parent_node.right)

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
            elif current_node.left is None:
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
        while (node is not None and
               (node.value < element or node.value > element)):
            node.sub_tree_size += 1
            previous_node = node
            if node.value < element:
                node = node.right
            elif node.value > element:
                node = node.left
            else:
                return
        node = Node(element, previous_node)
        if element > previous_node.value:
            previous_node.right = node
        else:
            previous_node.left = node
        self._update_balance(node)

    def count(self):
        if self.root is None:
            return 0
        return self.root.sub_tree_size

    def clear(self):
        self.root = None
