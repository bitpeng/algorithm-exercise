#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from random import randint as ri

# 给定一个字符串，只包含字母和空格，统计单词个数
def WordCount(s):
    inWord = False; cnt = 0
    for i in s:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            if inWord:pass
            else: cnt += 1; inWord = True
        else: inWord = False
    return cnt

a = ''.join([chr(ri(97, 122)) for i in range(200)])
for i in ['a','g', 'm', 'r', 'z']:
    a = a.replace(i, ' ')

print a
print WordCount(a)
print len(a.split())
a = [ri(0, 10) for i in range(10)]
b = [ri(0, 10) for i in range(10)]
a.sort(); b.sort()
print a, b

