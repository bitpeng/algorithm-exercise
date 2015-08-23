#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        #ListNode ret = pHead
        #ListNode ret
        ret = ListNode()
        ret.next = None
        #pHead = pHead.next
        while pHead:
            p = pHead
            pHead = p.next
            p.next = ret.next
            ret.next = p
        return ret.next
