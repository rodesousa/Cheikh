#!/usr/bin/env python3

from pattern import Pattern
from attributs import Attributs

class User(Pattern):

	def __init__(self,name_user):
		self.attributs = {}
		condition = self.check(name_user)
		if condition ==  True:
			for key in name_user:
				self.attributs[key]= name_user[key]

	def do(self):
		print ('NOT IMPLE')

	def check(self,name_user):
		return 'name' in name_user
