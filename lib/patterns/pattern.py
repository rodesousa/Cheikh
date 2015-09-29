#!/usr/bin/env python

import re


class Pattern(object):
    ATTRIBUTS = ['returns', 'name','expected']

    def __init__(self, name, arguments_attribut):
        self.attributs = {}
        self.check_tag = {}
        self.name = name
        self.check_without_tag = {}
        if self.check_arg(arguments_attribut):
            self.check = True
            for key in arguments_attribut:
                if key in Pattern.ATTRIBUTS:
                    self.attributs[key] = arguments_attribut[key]
                else:
                    self.stderr = "The argument %s doesn't exist\n" % key
                    self.check = False
            self.add_default_attr(arguments_attribut)
        else:
            self.check = False
            self.stderr = "Name argument is absent or not arguments enough"

    def add_check_without_tag(self, name_attributs, attributs):
        for attr in name_attributs:
            if attr in attributs:
                self.check_without_tag[attr] = r'%s' %attributs[attr]

    def add_default_attr(self, arguments_attribut):
        if not 'returns' in arguments_attribut:
            self.attributs['returns'] = ''
        else:
            self.check_without_tag['returns'] = r'%s' %self.attributs['returns']
        if not 'expected' in arguments_attribut:
            self.expected = True
        else:
            if arguments_attribut['expected'] == 'false' or arguments_attribut['expected'] == False or arguments_attribut['expected'] == 'False' or arguments_attribut['expected'] == 'FALSE':
               self.expected = False
            else:
                self.check = False
                self.stderr = "Bad value for expected (T|true or F|false)"


    def __str__(self):
        if self.check:
            return "%s %s: True" % (self.name, self.attributs['name'])
        return self.printError()

    def printError(self):
        if 'name' in self.attributs:
            return "ERROR %s %s: %s" % (self.name, self.attributs['name'], self.stderr)
        return "ERROR %s UNKNOW: %s" % (self.name, self.stderr)

    # Rentre la fonction un peu plus fonctionnelle
    def returns(self, returns):
        stdout_print = map(lambda (x,y): str(x.readlines()), returns)
        stderr_print = map(lambda (x,y): y.readlines(), returns)
        if self.returns_clasic(stderr_print):
            if self.returns_without_tag(stdout_print):
                self.returns_with_tag(stdout_print)
    #    if self.check and self.expected == False:
        if self.check and not self.expected:
            self.check = False
            self.stderr = "The test is %s but the expected value is %s" %(self.check, self.expected)
        # on force le self.check a true quand on attend un resultat faux
        elif not self.check and not self.expected:
            self.check = True
        return self.check

    def returns_with_tag(self, stdout_print):
        if self.check_tag:
            for key in self.check_tag:
                m = filter(lambda x: x is not None, map(lambda x : re.search(self.check_tag[key], x), stdout_print))
                if not re.search(m[0].group('tag'), self.attributs[key]):
                    self.check = False
                    self.stderr = "Isn't a good %s : %s != %s " % ( \
                            key, m[0].group('tag'), self.attributs[key])
        return self.check
       
    def returns_without_tag(self, stdout_print):
        if self.check_without_tag:
            for key in self.check_without_tag:
                if not filter(lambda x: x is not None, map(lambda x : re.search(self.check_without_tag[key], x), stdout_print)):
                    self.check = False
                    self.stderr = "Argument %s doesn't true" % key
        return self.check

    def returns_clasic(self, stderr_print):
        tmp = filter(lambda x: len(x)>0 , stderr_print)
        if tmp:
            self.check = False
            self.stderr = tmp[0][0]
            
        return self.check

    def check_arg(self, arguments_attribut):
        print 'MUST BE IMPLEMENTED'
        return True
