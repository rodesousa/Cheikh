#!/usr/bin/env python

def genere_trace_localhost(cptTrue, cptFalse, lenPatterns, isVerbose, strPattern):
    return genere_trace(cptTrue, cptFalse, lenPatterns, 'localhost', isVerbose, strPattern)


def genere_trace(cptTrue, cptFalse, lenPatterns, host, isVerbose, strPattern):
    tmp = "\n---%s---\n" % host
    tmp += "Good= %s/%s\n" % (cptTrue, lenPatterns)
    if cptFalse != 0:
        tmp += "Fail= %s/%s\n" % (cptFalse, lenPatterns)
    if isVerbose or cptFalse != 0:
        tmp += "###Detail###\n"
    return tmp + strPattern
