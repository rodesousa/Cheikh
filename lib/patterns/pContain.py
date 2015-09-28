#!/usr/bin/python

from pattern import *


class PContain(Pattern):
    Pattern.ATTRIBUTS.extend(['name', 'exp'])

    def __init__(self, arguments_attribut):
        super(PContain, self).__init__('PContain', arguments_attribut)
        if self.check:
            self.check_without_tag['returns'] = r'True'

    def do(self):
        return ["cat %s | grep %s && echo True" %(self.attributs['name'], self.attributs['exp'])]

    def check_arg(self, arguments_attribut):
        if 'name' in arguments_attribut and 'exp' in arguments_attribut:
            return True
        return False
