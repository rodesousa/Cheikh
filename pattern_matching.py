#!/usr/bin/env python3

#
#Code provisoire. Chercher des fonctions de pattern matching où la dvp
#
from user import User


def pattern_matching(data_yaml):
		list_pattern = []
		for key in data_yaml:
			if key == 'user':
				user = User(data_yaml[key])
				list_pattern.append(user)
