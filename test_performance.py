#!/usr/bin/env python3
import sys
import os
import time
import argparse
from modules import linear_search
from modules import ordered_array
from modules import binary_tree
from modules import balanced_tree
from modules import hash_table
from tests import average_measurements
from tests import worst_measurements
from tests import best_measurements


def main():
    parser = create_parser()
    args = input('Input new args: ').split()
    parsed_args = parser.parse_args(args)
    dictionaries, data, test_type = treat_args(parsed_args)
    if data is None:
        raise ValueError('No arguments were get, check your arguments')
    if test_type == 'average_measurements':
        for dictionary in dictionaries:
            for file_name in data:
                parsed_data = []
                with open(os.path
                          .join("{0}//{1}"
                                .format(parsed_args.average_measurements,
                                        file_name)), 'r') as file:
                    parsed_data = file.read().split()
                tests = average_measurements.Average_measurements(dictionary,
                                                                  parsed_data)
                print(file_name, type(dictionary).__name__)
                run_measurements(tests)
                tests.dictionary.clear()
                print()
    elif test_type == 'best_measurements' or test_type == 'worst_measurements':
        for dictionary in dictionaries:
            for data_size in data:
                elements = _generate_data(data_size)
                print(type(dictionary).__name__, data_size)
                tests = _get_tests_for_dict(dictionary, test_type, elements)
                run_measurements(tests)
                dictionary.clear()
                print()
    return


def treat_args(parsed_args):
    dictionaries = []
    data = []
    test_type = ''
    if parsed_args.dictionary_type:
        dictionaries = _get_selected_dictionary(parsed_args.dictionary_type)
        dict_type = parsed_args.dictionary_type
    if parsed_args.worst_measurements:
        data = parsed_args.worst_measurements
        test_type = 'worst_measurements'
    elif parsed_args.best_measurements:
        data = parsed_args.best_measurements
        test_type = 'best_measurements'
    elif parsed_args.average_measurements:
        path = parsed_args.average_measurements
        data = os.listdir(os.path.join(path))
        test_type = 'average_measurements'
    return (dictionaries, data, test_type)


def _get_selected_dictionary(dictionary_type):
    dictionaries = []
    comparer = {'linear_search': linear_search.Linear_search,
                'ordered_array': ordered_array.Ordered_array,
                'binary_tree':  binary_tree.Binary_tree,
                'balanced_tree': balanced_tree.Balanced_tree,
                'hash_table': hash_table.Hash_table}
    if dictionary_type == 'dict':
        dictionaries.append({})
    elif dictionary_type == 'all':
        dictionaries = [{}]
        for dict_type in comparer:
            dictionaries.append(comparer[dict_type]('str'))
    else:
        dictionaries.append(comparer[dictionary_type]('str'))
    return dictionaries


def _generate_data(data_size):
    data = []
    num = 1
    for i in range(data_size):
        data.append(num)
        num += 1
    return data


def _get_tests_for_dict(dictionary, test_type, data):
    tests = None
    worst_comparer = {
        'linear_search': worst_measurements.Worst_linear_search_measurements,
        'ordered_array': worst_measurements.Worst_ordered_array_measurements,
        'binary_tree': worst_measurements.Worst_binary_tree_measurements,
        'balanced_tree': worst_measurements.Worst_balanced_tree_measurements,
        'hash_table': worst_measurements.Worst_hash_table_measurements,
        'dict': worst_measurements.Worst_dict_measurements}
    best_comparer = {
        'linear_search': best_measurements.Best_linear_search_measurements,
        'ordered_array': best_measurements.Best_ordered_array_measurements,
        'binary_tree': best_measurements.Best_binary_tree_measurements,
        'balanced_tree': best_measurements.Best_balanced_tree_measurements,
        'hash_table': best_measurements.Best_hash_table_measurements,
        'dict': best_measurements.Best_dict_measurements}
    if test_type == 'worst_measurements':
        tests = worst_comparer[type(dictionary).__name__.lower()](data)
    elif test_type == 'best_measurements':
        tests = best_comparer[type(dictionary).__name__.lower()](data)
    return tests


def create_parser():
    parser = argparse.ArgumentParser(
        description='Console version for start testing\n\
                     \rThe list of keys:\n\
                     \r-wm\n\
                     \r-bm\n\
                     \r-am\n\
                     \r-dt')
    parser.add_argument('-wm', '--worst_measurements',
                        type=int, action='append',
                        help='running worst tests with selected data sizes')
    parser.add_argument('-bm', '--best_measurements',
                        type=int, action='append',
                        help='running best tests with selected data sizes')
    parser.add_argument('-am', '--average_measurements',
                        type=str,
                        help='running tests for files in selected folder')
    parser.add_argument('-dt', '--dictionary_type',
                        type=str,
                        help='choosing type of dictionary\n\
                              \rprint "all" for start every dictionary tests')
    return parser


def run_measurements(tester):
    tests = [tester.test_append, tester.test_element, tester.test_index_of,
             tester.test_contains, tester.test_insert, tester.test_delete]
    for test in tests:
        start = time.time()
        test()
        print('{0} works: {1}seconds'
              .format(test.__name__,
                      (time.time() - start) / len(tester.elements)))
        dict_size = 0
        if type(tester.dictionary) is linear_search.Linear_search:
            dict_size = sys.getsizeof(tester.dictionary.array)
        elif type(tester.dictionary) is ordered_array.Ordered_array:
            dict_size = sys.getsizeof(tester.dictionary.ord_array)
        elif (type(tester.dictionary) is binary_tree.Binary_tree or
              type(tester.dictionary) is balanced_tree.Balanced_tree):
            dict_size = sys.getsizeof(tester.dictionary.root)
            dict_size *= tester.dictionary.root.sub_tree_size
        elif type(tester.dictionary) is hash_table.Hash_table:
            dict_size = sys.getsizeof(tester.dictionary.table)
            for value in tester.dictionary.table.values():
                dict_size += sys.getsizeof(value)
        else:
            dict_size = sys.getsizeof(tester.dictionary)
        print('The size of dictionary in bytes: {0}'.format(dict_size))
    return

if __name__ == '__main__':
    main()
