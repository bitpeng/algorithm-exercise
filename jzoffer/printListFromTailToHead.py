#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
  输入一个链表，从尾到头打印链表每个节点的值。
  测试用例:
  {}
  
  对应输出应该为:
  []
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return None
        if not listNode:
            return []
        ret = [listNode.val]
        p = listNode.next
        while p:
            #ret.append(p.val)
            ret.insert(0, p.val)
            p = p.next

        return ret


s = Solution()
print s.printListFromTailToHead({})
