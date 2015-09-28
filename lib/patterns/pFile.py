#!/usr/bin/python

from pattern import *

class PFile(Pattern):
    Pattern.ATTRIBUTS.extend(['name', 'state', 'size', 'type', 'path', 'owner', 'chmod'])

    def __init__(self, arguments_attribut):
        super(PFile, self).__init__('Pfile', arguments_attribut)
        if self.check:
            if 'state' not in self.attributs:
                self.attributs['state'] = 'exist'

            if 'type' not in self.attributs:
                self.attributs['type'] = 'file'

            self.add_check_without_tag(['size', 'owner', 'group'], arguments_attribut)

            if 'chmod' in self.attributs:
                self.check_without_tag['chmod'] = self.convert_chmod(self.attributs['chmod'])

            if self.attributs['type'] == 'file':
                self.attributs['MA_GROSSE_TEUB'] = 'e'
            elif self.attributs['type'] == 'directory':
                self.attributs['MA_GROSSE_TEUB'] = 'd'

            self.check_without_tag['type'] = r"True"

    def do(self):
        return ["ls -l %s | grep %s | awk '{print $1" "$3" "$5" "$6}'" %(self.attributs['path'], self.attributs['name']), 'test -%s %s/%s && echo True'%(self.attributs['MA_GROSSE_TEUB'], self.attributs['path'], self.attributs['name']) ]

    def check_arg(self, arguments_attribut):
        if 'name' in arguments_attribut and 'path' in arguments_attribut:
            return True
        return False

    def convert_chmod(self, permision):
        mode = r""
        for i in str(permision):
            if i == '0' : mode += '---'
            if i == '1' : mode += '--x'
            if i == '2' : mode += '-w-'
            if i == '3' : mode += '-wx'
            if i == '4' : mode += 'r--'
            if i == '5' : mode += 'r-x'
            if i == '6' : mode += 'rw-'
            if i == '7' : mode += 'rwx'
        return mode
