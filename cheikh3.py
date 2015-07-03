#!/usr/bin/env python3

import sys, yaml, os

sys.path.append('lib')
sys.path.append('lib/patterns')

from engine import *
from pattern_matching import *

#VERIFICATION
if len(sys.argv) > 3 or len(sys.argv) < 2:
	print ('Problème sur le nombre d\'arguments')
	sys.exit(1)

if not os.path.isfile(sys.argv[1]):
	print ('Le chemin est incorrecte')

if len(sys.argv) == 3:
	engine = sys.argv[2]

if not 'engine' in locals():
	engine = "l"

#READ YAMl
stream = open(sys.argv[1],'r')
data_yaml = yaml.load(stream)

#PATTERN_MATCHING
patterns = pattern_matching(data_yaml) 	

#ENGINE
if engine == 'l' or engine == 'local' or engine == 'localhost':
	print(engine_localhost(patterns))

elif engine == 'ssh':
	stream_config= open('config.yaml')
	config = yaml.load(stream_config)
	print(engine_ssh(patterns,config))
else:
	print("L\'argument %s n\'est pas supporté" %engine)
