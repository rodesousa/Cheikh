#!/usr/bin/python

import argparse

def check_args():
  parser = argparse.ArgumentParser(description='script to check environment status')

  parser.add_argument('yamlFile', help="yaml file containing environment checks")

  parser.add_argument('-v', '--verbose',
    action="store_true",
    default=False, 
    help="verbose output" )

  parser.add_argument('-s', '--ssh', nargs='?',const='config.yaml', default=False,
  #parser.add_argument('-s', '--ssh', 
    help="ssh check environment" )

  parser.add_argument('-l', '--local', '--localhost', 
    action="store_true",
    default=False,
    help="localhost check environment" )
  return parser
