# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []
        self.min_stack = []
    def push(self, node):
        # write code here
        self.data.append(node)
        if len(self.min_stack) == 0:
            self.min_stack.append(node)
        else:
            _min = self.min()
            if _min > node:
                self.min_stack.append(node)
            else:
                self.min_stack.append(_min)
    def pop(self):
        # write code here
        if not self.data:
            return
        self.data.pop()
        self.min_stack.pop()
    def top(self):
        # write code here
        if not self.data:
            return None
        else:
            return self.data[-1]
    def min(self):
        # write code here
        if not self.data:
            return None
        else:
            return self.min_stack[-1]