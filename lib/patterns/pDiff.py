#!/usr/bin/python

from pattern import *


class PDiff(Pattern):
    Pattern.ATTRIBUTS.extend(['name', 'name_1', 'name_2'])

    def __init__(self, arguments_attribut):
        super(PDiff, self).__init__('PDiff', arguments_attribut)
        if self.check:
            self.attributs['name'] = self.attributs['name_1'] + self.attributs['name_1'] 
            self.check_without_tag['returns'] = r'True'

    def do(self):
        return ["diff -q %s %s && echo True" %(self.attributs['name_1'], self.attributs['name_2'])]

    def check_arg(self, arguments_attribut):
        if 'name_1' in arguments_attribut and 'name_2' in arguments_attribut:
            return True
        return False

