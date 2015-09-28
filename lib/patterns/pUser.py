#!/usr/bin/python

from pattern import *


class PUser(Pattern):
    Pattern.ATTRIBUTS.extend(['name', 'uid', 'gid'])

    def __init__(self, arguments_attribut):
        super(PUser, self).__init__('User', arguments_attribut)

        if self.check:
            if 'uid' in self.attributs:
                self.check_tag['uid'] = r"uid=(?P<tag>[\d]+)"
            if 'gid' in self.attributs:
                self.check_tag['gid'] = r"gid=(?P<tag>[\d]+)"

    def do(self):
        return ['id %s' % self.attributs['name']]

    def check_arg(self, arguments_attribut):
        if 'name' in arguments_attribut:
            return True
        return False
