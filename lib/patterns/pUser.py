#!/usr/bin/python

from pattern import *


class PUser(Pattern):
    Pattern.ATTRIBUTS.extend(['name', 'uid', 'gid'])
    Pattern.NAME = 'User'

    def __init__(self, name_user):
        super(PUser, self).__init__(name_user)

    # On retourne (String) toutes les potentielles commande shell possible avec le pattern. 
    def do(self):
        if 'name' in self.attributs:
            return 'id %s' % self.attributs['name']
        return 'id %s' % self.attributs['uid']

    # Dans l'argument name_user, on regarde si il y a au moins 1 commande possible.
    def check(self, name_user):
        if 'uid' in name_user or 'name' in name_user:
            return True
        return False
