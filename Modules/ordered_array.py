import utils


class Ordered_array:
    def __init__(self, elements_type):
        self.ord_array = []
        (ok, msg) = utils.check_type(elements_type)
        if not ok:
            raise ValueError(msg)
        self.elements_type = msg

    def append(self, element):
        if isinstance(utils.try_lead_to(element, self.elements_type), self.elements_type):
            self.ord_array.append(element)
            self.ord_array.sort()

    def element(self, index):
        index = utils.parse_int(index)
        if index is None or len(self.ord_array) <= index or index < 0:
            raise ValueError()
        return self.ord_array[index]

    def index_of(self, element):
        i = 0
        j = len(self.ord_array) - 1
        m = int(j / 2)
        while self.ord_array[m] != element and i < j:
            if element > self.ord_array[m]:
                i = m + 1
            else:
                j = m - 1
            m = int((i + j) / 2)
        if i > j:
            return -1
        return m

    def contains(self, element):
        if self.index_of(element) == -1:
            return False
        return True
