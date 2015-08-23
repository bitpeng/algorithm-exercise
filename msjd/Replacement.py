# -*- coding:utf-8 -*-

class Replacement:
    def replaceSpace(self, iniString, length):
        # write code here
        s = iniString[:]
        return s.replace(' ', '%20')




ins = Replacement()
s = ins.replaceSpace('qw', 2)
print s
