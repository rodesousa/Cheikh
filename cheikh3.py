#!/usr/bin/env python3

import sys, yaml, os

from pattern_matching import *

#VERIFICATION
if len(sys.argv) != 2:
	print ('Il faut 2 arguments !')
	sys.exit(1)

if not os.path.isfile(sys.argv[1]):
	print ('Le chemin est incorecte')

#READ YAMl
file_yaml = sys.argv[1]
stream = open(file_yaml,'r')
data_yaml = yaml.load(stream)

#PATTERN_MATCHING
pattern_matching(data_yaml) 	
