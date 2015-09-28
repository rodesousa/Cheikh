#!/usr/bin/python

from pattern import *


class PService(Pattern):
    Pattern.ATTRIBUTS.extend(['name', 'status'])

    def __init__(self, arguments_attribut):
        super(PService, self).__init__('Service', arguments_attribut)

        if self.check:
            if self.attributs['status'] == 'start':
                self.check_without_tag['status'] = 'running'
            elif self.attributs['status'] == 'stop':
                self.check_without_tag['status'] = 'stop'

    def do(self):
        return ['/etc/init.d/%s status' % self.attributs['name']]

    def check_arg(self, arguments_attribut):
        if 'name' in arguments_attribut and 'status' in arguments_attribut:
            return True
        return False
