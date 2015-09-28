#!/usr/bin/python

from pattern import *


class PPackage(Pattern):
    Pattern.ATTRIBUTS.extend(['installed', 'name', 'version', 'mode'])

    def __init__(self, arguments_attribut):
        super(PPackage, self).__init__('Package', arguments_attribut)
        if self.check:
            if not 'installed' in self.attributs:
               self.attributs['installed'] = 'yes'

            if 'version' in self.attributs:
               self.check_tag['version'] = r"Version[ ]*:[ ]*(?P<tag>[\w.:]+)"

            if self.attributs['mode'] == 'yum':
                if self.attributs['installed'] == 'yes':
                   self.check_without_tag['installed'] = r"Repo[ ]*: installed"
                else: 
                   self.check_without_tag['installed'] = r"Repo[ ]*: (?!installed)"

    def do(self):
        if self.attributs['mode'] == 'yum':
            return ["yum info %s" % self.attributs['name']]
        elif self.attributs['mode'] == 'apt':
            return ["apt-cache show %s" % self.attributs['name'], 'dpkg -l %s' %self.attributs['name']]

    def check_arg(self, arguments_attribut):
        if 'name' in arguments_attribut and \
                        'mode' in arguments_attribut:
            return True
        return False
