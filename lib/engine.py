#!/usr/bin/env python3

import subprocess, os, paramiko
from pattern import Pattern
from paramiko import SSHClient

def engine_localhost(patterns):
                print('engine_localhost')
                resp = ""
                for pattern in patterns:
                        stdout = ''
                        return_ = subprocess.Popen(str.split(pattern.do(),' '),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                        resp= resp + pattern.print(return_.stdout,return_.stderr)
                return resp

def engine_ssh(patterns,config):
                print('engine_ssh')
                resp = ""
                client = SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                servers= config['server']
                for key in servers:
                   client.connect(servers[key]['hostname'],username=servers[key]['user'],password=servers[key]['password'])
                   for pattern in patterns:
                      stdin, stdout, stderr = client.exec_command(pattern.do())
                      resp = resp + pattern.print(stdout,stderr)
                return resp
