#!/usr/bin/python

from pattern import *


class PWget(Pattern):
    Pattern.ATTRIBUTS.extend(['name', 'url', 'protocole'])

    def __init__(self, arguments_attribut):
        super(PWget, self).__init__('PWget', arguments_attribut)
        if self.check:
            self.attributs['name'] = self.attributs['url']

    def do(self):
        return ["wget --spider %s://%s 2>&1" %(self.attributs['protocole'], self.attributs['url'])]

    def check_arg(self, arguments_attribut):
        if 'url' in arguments_attribut and 'protocole' in arguments_attribut:
            return True
        return False



