import sys
import utils
from i_dict import i_dict


class Hash_table(i_dict):
    def __init__(self, elements_type):
        self.table = []
        # const - some of primary number for generating hash.
        self.const = 991
        (ok, msg) = utils.check_type(elements_type)
        if not ok:
            raise ValueError(msg)
        self.elements_type = msg

    def append(self, element):
        element_hash = get_hash(element)
        try:
            if self.elements_type is float:
                self.table.insert(float(element), element_hash)
            elif self.elements_type is str:
                self.table.insert(str(element), element_hash)
            elif self.elements_type is int:
                self.table.insert(int(element), element_hash)
        except:
                print('Not correct element type{0}\
                       Should be{1}'.format(type(element), self.elements_type))
        return

    def element(self, index):
        print('Hash table is not working with index')
        return

    def index_of(self, element):
        return get_hash(element)

    def contains(self, element):
        try:
            self.table(get_hash(element))
            return True
        except:
            return False

    def get_hash(self, element):
        element_hash = 0
        element_str = str(element)
        for char in element_str:
            element_hash = ((element_hash * self.const + ord(char)) %
                            len(element_str))

