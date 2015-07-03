#!/usr/bin/env python3

from pattern import Pattern
from attribut import Attribut

class Curl(Pattern):

   def __init__(self,name_user):
      self.attributs = {}
      if self.check(name_user) ==  True:
         for key in name_user:
            if self.possibleArguments(key) :
               self.attributs[key]= name_user[key]
         if 'returns' not in name_user:
            self.attributs['returns']= 0 

   def do(self):
      return ['curl',self.attributs['url']]

#A FAIRE
   def possibleArguments(self,arg):
      return True

   def check(self,name_user):
      return 'url' in name_user

   def print(self,value_check):
      resp = self.returns(value_check)
      return ("curl %s: %s \n") %(self.attributs['url'],resp)

   def returns(self,value_check):
      return self.attributs['returns'] == value_check
