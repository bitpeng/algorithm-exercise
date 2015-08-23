#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
    题目描述

    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        # if number <= 0:
        #     return 0
        # elif number == 1:
        #     return 1
        # else:
        #     return self.jumpFloor(number -2) + self.jumpFloor(number - 1)
        a = 1
        b = 2
        if number <=0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2

        for i in xrange(3, number + 1):
            a, b = b, a + b
        return b

