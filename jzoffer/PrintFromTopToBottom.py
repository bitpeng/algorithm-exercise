#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from collections import deque
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
        # 返回从上到下每个节点值列表，例：[1,2,3]
        def PrintFromTopToBottom(self, root):
            # write code here 
            from collections import deque
            if root is None:
                return None
            if not root:
                return []

            q = deque()
            q.append(root)
            ret = []
            while True:
                node = q.popleft()
                ret.append(node.val)
                if node.left:
                    q.append(node.left)
                q.append(node.right) if node.right else pass
            return ret


