#!/usr/bin/python

import sys

sys.path.append('lib/patterns')
sys.path.append('patterns')


# data_yaml : fichier de conf yaml en liste
# itere sur les pattern dans le yaml, tente d'importer les patterns, et si c'est possible, initialise la class
def pattern_matching(data_yaml):
    list_pattern = []
    for key in data_yaml:
        pattern = key.popitem()
        key_pattern = pattern[0][0].upper() + pattern[0][1:]
        module_pattern = __import__('p' + key_pattern)
        class_pattern = getattr(module_pattern, 'P' + key_pattern)
        if 'name' in pattern[1] and isinstance(pattern[1]['name'], list):
            pattern_class = class_pattern(pattern[1])
            list_pattern = list_pattern + pattern_class
        else:
            list_pattern.append(class_pattern(pattern[1]))
    return list_pattern

