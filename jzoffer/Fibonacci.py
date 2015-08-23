#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
  测试用例:
  1

  对应输出应该为:
  1
  测试用例:
  0

  对应输出应该为:
  0
'''

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 0:
            return 0
        if n == 1:
            return 1

        a = 0
        b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return a
