#!/usr/bin/python

from pattern import *


class PPgrep(Pattern):
    Pattern.ATTRIBUTS.extend(['name', 'user'])

    def __init__(self, arguments_attribut):
        super(PPgrep, self).__init__('Ppgrep', arguments_attribut)
        if self.check:
            self.check_without_tag['returns'] = r'True'

    def do(self):
        if 'name' in self.attributs:
            if 'user' in self.attributs:
                return ['pgrep -u %s %s && echo "True"' %(self.attributs['user'], self.attributs['name'])]
            else:
                return ['pgrep %s && echo "True"' %(self.attributs['name'])]
                

    def check_arg(self, arguments_attribut):
        if 'name' in arguments_attribut:
            return True
        return False

