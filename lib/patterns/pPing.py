#!/usr/bin/python

from pattern import *


class PPing(Pattern):
    Pattern.ATTRIBUTS.extend(['name'])

    def __init__(self, arguments_attribut):
        super(PPing, self).__init__('Ping', arguments_attribut)
        if self.check:
            self.check_without_tag['returns'] = r'True'

    def do(self):
        return ['nslookup %s && echo True' % self.attributs['name']]

    def check_arg(self, arguments_attribut):
        if 'name' in arguments_attribut:
            return True
        return False

