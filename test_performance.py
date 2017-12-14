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
    dict_types = 'dict'
    dictionary = {}
    if dict_types == 'linear_search':
        dictionary = linear_search.Linear_search('str')
    elif dict_types == 'ordered_array':
        dictionary = ordered_array.Ordered_array('str')
    elif dict_types == 'binary_tree':
        dictionary = binary_tree.Binary_tree('str')
    elif dict_types == 'balanced_tree':
        dictionary = balanced_tree.Balanced_tree('str')
    elif dict_types == 'hash_table':
        dictionary = hash_table.Hash_table('str')

    am = average_measurements.Average_measurements(dictionary, path)
    run_measurements(am)
    return


def create_parser():
    parser = argparse.ArgumentParser(
        description='Console version of games_of_life:\n\
                    \rThe list of keys:\n\
                    \r-g\n\
                    \r-k\n\
                    \r-ps\n\
                    \r-phm\n\
                    \r-ns\n\
                    \r-pf\n\
                    \r-chr\n\
                    \r-cld\n\
                    \r-ct\n\
                    \r-cs\n\
                    \r-ccs')
    return parser


def run_measurements(am):
    tests = [am.test_append, am.test_element, am.test_index_of,
             am.test_contains, am.test_insert, am.test_delete]
    for test in tests:
        start = time.time()
        test()
        print('{0} works: {1}seconds'
              .format(test.__name__,
                      round((time.time() - start) / len(am.elements), 10)))
        dict_size = 0
        if type(am.dictionary) is linear_search.Linear_search:
            dict_size = sys.getsizeof(am.dictionary.array)
        elif type(am.dictionary) is ordered_array.Ordered_array:
            dict_size = sys.getsizeof(am.dictionary.ord_array)
        elif (type(am.dictionary) is binary_tree.Binary_tree or
              type(am.dictionary) is balanced_tree.Balanced_tree):
            dict_size = sys.getsizeof(am.dictionary.root)
            dict_size *= am.dictionary.root.sub_tree_size
        elif type(am.dictionary) is hash_tabl.eHash_table:
            dict_size = sys.getsizeof(am.dictionary.table)
        else:
            dict_size = sys.getsizeof(am.dictionary)
        print('The size of dictionary in bytes: {0}'.format(dict_size))
    return

if __name__ == '__main__':
    main()
