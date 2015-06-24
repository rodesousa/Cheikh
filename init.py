#!/usr/bin/env python
import yaml

with open("test.yaml", 'r') as stream:
    print(yaml.load(stream))
