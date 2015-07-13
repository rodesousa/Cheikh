#!/usr/bin/python

from pattern import Pattern

class PUser(Pattern):

   def __init__(self,name_user):
      self.attributs = {}
      condition = self.check(name_user)
      if condition ==  True:
         self.check= True
         self.stderr= ''
         for key in name_user:
           self.attributs[key]= name_user[key]
         self.attributs['returns']= True

   def do(self):
      return 'id %s' %self.attributs['name']

   def check(self,name_user):
      return 'name' in name_user

   def __str__(self):
      if self.check:
         return "User %s: True" %self.attributs['name']
      else :
         return self.printError()

   def printError(self):
         return "ERROR user %s: %s" %(self.attributs['name'],self.stderr)

   def returns(self,stdout,stderr):
      if self.attributs['returns']:
         error= stderr.readlines()
         if error:
           self.check= False
           self.stderr= error
      else:
         print 'NOT IMPLEM'
