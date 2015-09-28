#!/usr/bin/python

from pListe import *

class PContains(PListe):

    def __init__(self, arguments_attribut):
        super(PContains, self).__init__(arguments_attribut, 'Contain')
