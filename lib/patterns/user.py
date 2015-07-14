#!/usr/bin/env python3

from pattern import Pattern


class User(Pattern):

   def __init__(self,name_user):
      self.attributs = {}
      condition = self.check(name_user)
      if condition ==  True:
         for key in name_user:
            self.attributs[key]= name_user[key]
         self.attributs['returns']= True

   def do(self):
      return 'id %s' %self.attributs['name']
#      return ['id',self.attributs['name']]

   def check(self,name_user):
      return 'name' in name_user

   def printe(self,stdout,stderr):
      resp = self.returns(stdout,stderr)
      return ("user %s: %s \n") %(self.attributs['name'],resp)

   def returns(self,stdout,stderr):
      if self.attributs['returns']:
         return not stderr.readlines()
      else:
         return False
        #NOT IMPLEM
