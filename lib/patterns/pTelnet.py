#!/usr/bin/python

from pattern import *


class PTelnet(Pattern):
    Pattern.ATTRIBUTS.extend(['name', 'port'])

    def __init__(self, arguments_attribut):
        super(PTelnet, self).__init__('PTelnet', arguments_attribut)
        if self.check:
            self.check_without_tag['returns'] = r'True'

    def do(self):
        return ["nc -zv %s %s && echo 'True'" %(self.attributs['name'], self.attributs['port'])]

    def check_arg(self, arguments_attribut):
        if 'name' in arguments_attribut and 'port' in arguments_attribut:
            return True
        return False


