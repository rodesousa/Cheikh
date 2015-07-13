#!/usr/bin/env python

import subprocess, sys, os, paramiko
sys.path.append('lib')
sys.path.append('lib/patterns')
from pattern import Pattern
from paramiko import SSHClient
from printer import *

def engine_localhost(patterns,lvlPrint):
                strPattern = ""
                cptTrue= 0
                cptFalse= 0
                for pattern in patterns:
                        stdout = ''
                        return_ = subprocess.Popen(str.split(pattern.do(),' '),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                        pattern.returns(return_.stdout,return_.stderr)
                        if pattern.check:
                           cptTrue+=1
                        else:
                           cptFalse+=1
                        if lvlPrint or pattern.check == False:
                           strPattern+= "%s \n" %pattern
                return genere_trace_localhost(cptTrue, cptFalse, len(patterns), lvlPrint, strPattern)

def engine_ssh(patterns,config,lvlPrint):
                client = SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                servers= config['server']
                tmp= ''
                for key in servers:
                   strPattern= ""
                   cptTrue= 0
                   cptFalse= 0
                   client.connect(servers[key]['hostname'],username=servers[key]['user'],password=servers[key]['password'])

                   for pattern in patterns:
                      stdin, stdout, stderr = client.exec_command(pattern.do())
                      pattern.returns(stdout,stderr)
                      if pattern.check:
                         cptTrue+=1
                      else:
                         cptFalse+=1
                      if lvlPrint or pattern.check == False:
                         strPattern+= "%s \n" %pattern
                   tmp+= genere_trace(cptTrue, cptFalse, len(patterns), servers[key]['hostname'], lvlPrint, strPattern)
                return tmp
