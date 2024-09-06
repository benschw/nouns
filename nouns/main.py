#!/bin/python3

import argparse

from nouns.processing import processing_handler
from nouns.settings import INPUT_NOUN_LIST_PATH, ABSTRACT_TRAINING_DATA_PATH, CONCRETE_TRAINING_DATA_PATH, \
    CONCRETE_OUT_PATH, ABSTRACT_OUT_PATH
from nouns.three_nouns import three_nouns_handler


def main(sub_cmd):

    if sub_cmd == 'process':
        processing_handler(INPUT_NOUN_LIST_PATH,
                           ABSTRACT_TRAINING_DATA_PATH, CONCRETE_TRAINING_DATA_PATH,
                           ABSTRACT_OUT_PATH, CONCRETE_OUT_PATH)
    elif sub_cmd == 'three-nouns':
        three_nouns_handler(ABSTRACT_OUT_PATH, CONCRETE_OUT_PATH)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='three nouns')
    sub_parsers = parser.add_subparsers(dest='sub_cmd', help='sub-command help')

    parser_process = sub_parsers.add_parser('process', help='process data')
    parser_three_nouns = sub_parsers.add_parser('three-nouns', help='three nouns prompt')

    args = parser.parse_args()
    main(args.sub_cmd)

