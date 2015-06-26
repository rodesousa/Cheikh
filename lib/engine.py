#!/usr/bin/env python3

import subprocess,os
from pattern import Pattern

def engine_localhost(patterns):
		resp = ""
		for pattern in patterns:
			return_ = subprocess.call(pattern.do(),stdout=subprocess.DEVNULL)
			resp= resp + pattern.print(return_)
		return resp
