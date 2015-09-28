#!/usr/bin/python

import argparse


#Toutes les options de cheikh
def check_args():
    parser = argparse.ArgumentParser(description='script to check environment status')

    parser.add_argument('yaml_file', help="yaml file containing environment checks")

    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        default=False,
                        help="verbose output")

    parser.add_argument('-l', '--local', '--localhost',
                        action="store_true",
                        default=False,
                        help="localhost check environment")

    parser.add_argument('-s', '--ssh', nargs='?', const='config.yaml',
                        default=False,
                        help="ssh check environment using conf_file",
                        metavar="conf_file")

    return parser
