import sys
import utils
from i_dict import i_dict


class Linear_search_array(i_dict):
    def __init__(self, elements_type):
        self.array = []
        (ok, msg) = utils.check_type(elements_type)
        if not ok:
            raise ValueError(msg)
        self.elements_type = msg

    def append(self, element):
        if isinstance(utils.try_lead_to(element, self.elements_type), self.elements_type):
            self.array.append(element)

    def element(self, index):
        index = utils.parse_int(index)
        if index is None or len(self.array) <= index or index < 0:
            raise ValueError()
        return self.array[index]

    def index_of(self, element):
        for i in range(len(self.array)):
            if self.array[i] == element:
                return i
        return -1

    def contains(self, element):
        if self.index_of(element) == -1:
            return False
        return True
