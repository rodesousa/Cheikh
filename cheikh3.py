#!/usr/bin/env python3

import sys, yaml, os

sys.path.append('lib')

from engine import *
from pattern_matching import *

#VERIFICATION
if len(sys.argv) != 2:
	print ('Il faut 2 arguments !')
	sys.exit(1)

if not os.path.isfile(sys.argv[1]):
	print ('Le chemin est incorrecte')

#READ YAMl
file_yaml = sys.argv[1]
stream = open(file_yaml,'r')
data_yaml = yaml.load(stream)

#PATTERN_MATCHING
patterns = pattern_matching(data_yaml) 	
print(engine_localhost(patterns))

