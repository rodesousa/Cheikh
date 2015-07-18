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

def genere_trace_localhost(cptTrue, cptFalse, lenPatterns, isVerbose, strPattern):
    return genere_trace(cptTrue, cptFalse, lenPatterns, 'localhost', isVerbose, strPattern)


def genere_trace(cptTrue, cptFalse, lenPatterns, host, isVerbose, strPattern):
    tmp = genere_color_trace(printer.UNDERLINE, "\n---%s---\n" % host)
    tmp += genere_color_trace(printer.OKGREEN, "Good= %s/%s\n" % (cptTrue, lenPatterns))
    if cptFalse != 0:
        tmp += genere_color_trace(printer.FAIL, "Fail= %s/%s\n" % (cptFalse, lenPatterns))
    if isVerbose or cptFalse != 0:
        tmp += genere_color_trace(printer.BOLD, "###Detail###\n")
    return tmp + strPattern


def genere_color_trace(color, message):
    return color + message + printer.ENDC
