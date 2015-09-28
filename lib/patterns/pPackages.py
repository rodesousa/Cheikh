#!/usr/bin/python

from pPackage import *


class PPackages(list):

    def __init__(self, arguments_attribut):
        super(PPackage, self).__init__(arguments_attribut, 'Package')
