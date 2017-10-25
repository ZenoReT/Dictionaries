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
            if current_node.value <= element:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return previous_node

    def append(self, element):
        if isinstance(utils.try_lead_to(element, self.elements_type), self.elements_type):
            if self.root.value is None:
                self.root.value = element
            else:
                parent_node = self._find_parent_for(element)
                if parent_node.value <= element:
                    parent_node.left = Node(element)
                else:
                    parent_node.right = Node(element)

    def element(self, index):
        index = utils.parse_int(index)
        if (self.root is None or index is None or
                self.root.sub_tree_size <= index or index < 0):
            raise ValueError()
        current_node = self.root
        while (not(current_node.left is not None and
                   current_node.left.sub_tree_size == index or
                   current_node.left is None and index <= 0)):
            if current_node.left and current_node.left.sub_tree_size > index:
                current_node = current_node.left
            elif current_node.left is None:
                index -= 1
                current_node = current_node.right
            else:
                index = index - 1 - current_node.left.sub_tree_size
                current_node = current_node.right
        return current_node.value

    def index_of(self, element):
        if not isinstance(utils.try_lead_to(element, self.elements_type), self.elements_type):
            raise ValueError()
        stack = [self.root]
        visited_nodes = set()
        while len(stack) != 0:
            current_node = stack.pop()
            if (current_node.left and
                    current_node in visited_nodes):
                stack.append(current_node.left)
            elif current_node.right:
                if current_node not in visited_nodes:
                    return current_node.value
                    visited_nodes.append(current_node)
                stack.append(current_node.right)
            else:
                return current_node.value
                visited_nodes.append(current_node)

    def contains(self, element):
        if isinstance(utils.try_lead_to(element, self.elements_type), self.elements_type):
            current_node = self.root
            while True:
                if current_node.value == element:
                    return True
                elif current_node.value > element and current_node.left:
                    current_node = current_node.left
                elif current_node.value <= element and current_node.right:
                    current_node = current_node.right
                else:
                    return False
