#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
  用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.q1 = []  # 用来入队
        self.q2 = []  # 用来出队

    def push(self, node):
        # write code here
        self.q1.append(node)

    def pop(self):
        # return xx
        if self.q2:
            return self.q2.pop()
        elif self.q1:
            self.q2 = self.q1[::-1]
            self.q1 = []
            return self.q2.pop()
        else:
            return None
