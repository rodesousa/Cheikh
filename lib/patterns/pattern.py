#!/usr/bin/env python

import re


class Pattern(object):
    ATTRIBUTS = ['returns']
    NAME = 'NOT IMPLEM'

    def __init__(self, name_user):
        self.attributs = {}
        if self.check(name_user):
            self.check = True
            self.stderr = ''
            for key in name_user:
                if key in Pattern.ATTRIBUTS:
                    self.attributs[key] = name_user[key]
                else:
                    print "The argument %s doesn't exist" % key
            if not 'returns' in self.attributs:
                self.attributs['returns'] = ''

    def __str__(self):
        if self.check:
            return "%s %s: True" % (Pattern.NAME, self.attributs['name'])
        return self.printError()

    def printError(self):
        return "ERROR %s %s: %s" % (Pattern.NAME, self.attributs['name'], self.stderr)

    def returns(self, stdout, stderr):
        if self.attributs['returns'] == '':
            error = stderr.readlines()
            if error:
                self.check = False
                self.stderr = error
        else:
            if re.search(self.attributs['returns'], str(stdout.readlines())) is None:
                self.check = False
                self.stderr = "%s doesn't find" % self.attributs['returns']

    def do(self):
        return 'MUST BE IMPLEMENTED'

    def check(self, name_user):
        print 'MUST BE IMPLEMENTED'
        return True
