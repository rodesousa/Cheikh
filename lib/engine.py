#!/usr/bin/env python

import subprocess
import sys

import paramiko

sys.path.append('lib')
sys.path.append('lib/patterns')

from paramiko import SSHClient
from printer import *

#Itere sur le nombre de server, ensuite sur les commandes a execute.
def engine_ssh(patterns, config, is_verbose):
    client = init_client_ssh()
    servers = config['server']
    tmp = ''
    for key in servers:
        try:
            str_pattern = ""
            cpt_true = 0
            cpt_false = 0
            client.connect(servers[key]['hostname'], username=servers[key]['user'], password=servers[key]['password'])
            returns = []
            for pattern in patterns:
                if pattern.check:
                    for cmd in pattern.do():
                        try:
                           stdin, stdout, stderr = client.exec_command(cmd)
                           returns.append([stdout, stderr])
                        except:
                           pattern.stderr = "Error while processing check for attributes : {0}".format(pattern.attributs)
                           pattern.check = False
                pattern.returns(returns)
                if pattern.check:
                    cpt_true += 1
                else:
                    cpt_false += 1
                    str_pattern += print_response(is_verbose, pattern)
            tmp += genere_trace(cpt_true, cpt_false, len(patterns), servers[key]['hostname'], is_verbose, str_pattern)
        except:
            print genere_color_trace(printer.FAIL, "Error while trying connect to : {0} with user '{1}'".format(\
                servers[key]['hostname'], servers[key]['user']))
        finally:
            client.close()
    return tmp

#init de la connexion
def init_client_ssh():
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return client

# on met ajoute la conf localhost
def engine_localhost(patterns, config, is_verbose):
    config['server'] = {}
    config['server']['localhost'] = config['localhost']
    return engine_ssh(patterns, config, is_verbose)

#affiche une reponse selon la verbosite
def print_response(is_verbose, pattern):
    if is_verbose and not pattern.check:
        return genere_color_trace(printer.FAIL, "%s \n" % pattern)
    elif is_verbose and pattern.check:
        return genere_color_trace(printer.OKBLUE, "%s \n" % pattern)
    elif not pattern.check:
        return genere_color_trace(printer.FAIL, "%s \n" % pattern)
    return ""
