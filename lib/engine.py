#!/usr/bin/env python

import subprocess
import sys

import paramiko

sys.path.append('lib')
sys.path.append('lib/patterns')

from paramiko import SSHClient
from printer import *


def engine_localhost(patterns, is_verbose):
    str_pattern = ""
    cpt_true = 0
    cpt_false = 0
    for pattern in patterns:
        stdout = ''
        return_ = subprocess.Popen(str.split(pattern.do(), ' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pattern.returns(return_.stdout, return_.stderr)
        if pattern.check:
            cpt_true += 1
        else:
            cpt_false += 1
        if is_verbose and not pattern.check:
            str_pattern += genere_color_trace(printer.FAIL, "%s \n" % pattern)
        elif is_verbose and pattern.check :
            str_pattern += genere_color_trace(printer.OKBLUE, "%s \n" % pattern)
        elif not pattern.check:
            str_pattern += genere_color_trace(printer.FAIL, "%s \n" % pattern)
    return genere_trace_localhost(cpt_true, cpt_false, len(patterns), is_verbose, str_pattern)


def engine_ssh(patterns, config, is_verbose):
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    servers = config['server']
    tmp = ''
    for key in servers:
        str_pattern = ""
        cpt_true = 0
        cpt_false = 0
        client.connect(servers[key]['hostname'], username=servers[key]['user'], password=servers[key]['password'])

        for pattern in patterns:
            stdin, stdout, stderr = client.exec_command(pattern.do())
            pattern.returns(stdout, stderr)
            if pattern.check:
                cpt_true += 1
            else:
                cpt_false += 1
            if is_verbose or not pattern.check:
                str_pattern += "%s \n" % pattern
        tmp += genere_trace(cpt_true, cpt_false, len(patterns), servers[key]['hostname'], is_verbose, str_pattern)
    return tmp
