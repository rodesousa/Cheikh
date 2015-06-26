#!/usr/bin/env python3

from pattern import Pattern
from attribut import Attribut

class User(Pattern):

   def __init__(self,name_user):
      self.attributs = {}
      condition = self.check(name_user)
      if condition ==  True:
         for key in name_user:
            self.attributs[key]= name_user[key]
         self.attributs['returns']= 0

   def do(self):
      return ['id',self.attributs['name']]

   def check(self,name_user):
      return 'name' in name_user

   def print(self,value_check):
      resp = self.returns(value_check)
      return ("user %s: %s") %(self.attributs['name'],resp)

   def returns(self,value_check):
      return self.attributs['returns'] == value_check
