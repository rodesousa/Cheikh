#!/usr/bin/python

import sys, yaml, os, argparse

sys.path.append('lib')
sys.path.append('lib/patterns')

from engine import *
from pattern_matching import *
from argumentParser import *

######################################
# Command Lie parser
#####################################

args = check_args().parse_args()

####################################
# Checks from command line
####################################

# yaml file
if not os.path.isfile(args.yamlFile):
  print'yamlFile not found or Invalid file path'
  sys.exit(1)
# verbose
isVerbose= args.verbose

# engine type
if args.ssh and args.local:
  print 'Please choose ssh or local mode'
  sys.exit(1)

if args.ssh: 
   engine = 'ssh'
   if not os.path.isfile(args.ssh):
      print'ssh config yamlFile not found pr Invalid file path'
      sys.exit(1)
   else :
      sshYamlFile=args.ssh
elif args.local:
   engine = 'localhost'

else:
  engine= 'localhost'

###################################
# Lanch cheikh
####################################
print 'Lanching cheikh in {0} engine mode'.format(engine) 
#print'sshYamlFile {}'.format(sshYamlFile)

#READ YAMl
stream = open(args.yamlFile,'r')
data_yaml = yaml.load(stream)

#PATTERN_MATCHING
patterns = pattern_matching(data_yaml)   

#ENGINE
if engine == 'localhost':
  print engine_localhost(patterns,isVerbose)
  
elif engine == 'ssh':
  stream_config= open('config.yaml')
  config = yaml.load(stream_config)
  print engine_ssh(patterns,config,isVerbose)