import sys
from sys import argv
import utils
from Modules import linear_search
from Modules import ordered_array
from Modules import binary_tree
from Modules import balanced_tree
import random
import time


def _generate(elements_type, args):
    generated_data = []
    count = 0
    if len(args) > 2:
        count = utils.parse_int(args[2])
    if count is None or count < 1:
        count = 1000

    if elements_type == "str":
        for i in range(count):
            generated_data.append("a" * i)
    elif elements_type == "int":
        for i in range(count):
            generated_data.append(random.randint(-100000, 100000))
    elif elements_type == "float":
        for i in range(count):
            generated_data.append(random.uniform(-100000, 100000))
    return generated_data


def print_help():
    print("common types: str, int, float")
    print("you can generate some elements entered in console 'generate' after type and count of elements")


def args_helper(args):
    elements_type = ""
    if utils.check_type(args[0]) is not None and len(args) > 1:
        elements_type = args[0]
        linear = linear_search.Linear_search_array(elements_type)
        ordered = ordered_array.Ordered_array(elements_type)
        binary = binary_tree.Binary_tree(elements_type)
        balanced = balanced_tree.Balanced_tree(elements_type)
        standart = dict()
        if args[1] == "generate":
            generated_data = _generate(elements_type, args)
            args = [elements_type]
            for i in range(0, len(generated_data)):
                linear.append(generated_data[i])
                ordered.append(generated_data[i])
                binary.append(generated_data[i])
                balanced.append(generated_data[i])
                standart[i] = generated_data[i]
                args.append(generated_data[i])
        else:
            for i in range(1, len(args)):
                linear.append(args[i])
                ordered.append(args[i])
                binary.append(args[i])
                balanced.append(args[i])
                standart[i - 1] = args[i]
        notify_the_time(args[1:], linear, "linear search")
        notify_the_time(args[1:], ordered, "ordered array")
        notify_the_time(args[1:], binary, "binary tree")
        notify_the_time(args[1:], balanced, "balanced tree")
        notify_the_time(args[1:], standart, "standart dictionary")
    elif args[0] == "help":
        print_help()
    else:
        raise ValueError()


def _get_elements_by_dict_type(dictionary, dict_type):
#   getsizeof()
    if dict_type == "linear search":
        return dictionary.array.__sizeof__()
    if dict_type == "ordered array":
        return dictionary.ord_array.__sizeof__()
    if dict_type == "binary tree" or dict_type == "balanced tree":
        return dictionary.root.sub_tree_size * dictionary.root.__sizeof__()
    return dictionary.__sizeof__()


def notify_the_time(args, dictionary, name):
    print("{0}:".format(name))
    if name != "standart dictionary":
        start = time.time()
        for i in range(len(args)):
            dictionary.element(i)
        print("find element at index: {0}".format(time.time() - start))

        start = time.time()
        for i in range(len(args)):
            dictionary.index_of(args[i])
        print("find index at element: {0}".format(time.time() - start))

        start = time.time()
        for i in range(len(args)):
            dictionary.contains(args[i])
        print("element contains: {0}".format(time.time() - start))

    else:
        start = time.time()
        for i in range(len(args)):
            dictionary[i]
        print("find element at index: {0}".format(time.time() - start))

        start = time.time()
        for i in range(len(args)):
            for item in dictionary.items():
                if item == args[i]:
                    break
        print("find index at element: {0}".format(time.time() - start))

        start = time.time()
        for i in range(len(args)):
            args[i] in dictionary
        print("element contains: {0}".format(time.time() - start))

    print("needed source: {0}".format(
        _get_elements_by_dict_type(dictionary, name)))
    print()


def main(args):
    print("welcome to dictionaries. If you want to get help, enter 'help'")
    print("first: enter the type of elements and elements")
    print()
    args_helper(args)


if __name__ == '__main__':
    if len(argv[1:]) > 0:
        main(argv[1:])
    else:
        print("You should print unless 1 arguments(type of elements and elements(generate) or help")
