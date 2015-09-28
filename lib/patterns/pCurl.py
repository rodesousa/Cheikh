#!/usr/bin/python

from pattern import *


class PCurl(Pattern):
    Pattern.ATTRIBUTS.extend(['name', 'url', 'protocole', 'descr', 'user'])

    def __init__(self, arguments_attribut):
        super(PCurl, self).__init__('PCurl', arguments_attribut)
            

    def do(self):
        if 'user' in self.attributs:
            return ["curl -u %s %s://%s --fail --silent --show-error" %(self.attributs['user'], self.attributs['protocole'], self.attributs['name'])]
        else:
            return ["curl %s://%s --fail --silent --show-error" %(self.attributs['protocole'], self.attributs['name'])]

    def check_arg(self, arguments_attribut):
        if 'name' in arguments_attribut and 'protocole' in arguments_attribut:
            return True
        return False
