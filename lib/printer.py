#!/usr/bin/env python


class printer:
    def __init__(self):
        pass

    BOLD = '\033[1m'
    FAIL = '\033[91m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    UNDERLINE = '\033[4m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


def genere_trace_localhost(cpt_true, cpt_false, len_patterns, is_verbose, str_pattern):
    return genere_trace(cpt_true, cpt_false, len_patterns, 'localhost', is_verbose, str_pattern)


def genere_trace(cpt_true, cpt_false, len_patterns, host, is_verbose, str_pattern):
    tmp = genere_color_trace(printer.UNDERLINE, "\n---%s---\n" % host)
    tmp += genere_color_trace(printer.OKGREEN, "Good= %s/%s\n" % (cpt_true, len_patterns))
    if cpt_false != 0:
        tmp += genere_color_trace(printer.FAIL, "Fail= %s/%s\n" % (cpt_false, len_patterns))
    if is_verbose or cpt_false != 0:
        tmp += genere_color_trace(printer.BOLD, "###Detail###\n")
    return tmp + str_pattern


def genere_color_trace(color, message):
    return color + message + printer.ENDC
