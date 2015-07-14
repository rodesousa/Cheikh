#!/usr/bin/python

#
# Code provisoire. Chercher des fonctions de pattern matching ou la dvp
#

import sys

sys.path.append('lib/patterns')
sys.path.append('patterns')

from pUser import PUser


def pattern_matching(data_yaml):
    list_pattern = []
    for key in data_yaml:
        if key == 'user':
            user = PUser(data_yaml[key])
            list_pattern.append(user)
        if key == 'users':
            if 'name' in data_yaml[key]:
                for i in data_yaml[key]['name'].split(','):
                    list_pattern.append(PUser({'name': i}))
    return list_pattern
