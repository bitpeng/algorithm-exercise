# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def depth(root):
    if root is None:
        return 0
    # deep = 1
    from collections import deque
    dq = deque()
    layer = 1
    dq.append((root, 1))
    while dq:
        node, layer = dq.popleft()
        deep = layer
        if node.left:
            dq.append(node.left, layer + 1)
        if node.right:
            dq.append(node.right, layer + 1)

    return deep


class Solution:
    def IsBalanced_Solution(self, root):
        # write code here
        if not root:
            return True
        leftDeep = depth(root.left)
        rightDeep = depth(root.right)

        return -1 <= leftDeep - rightDeep <= 1


so = Solution()
root = TreeNode(6)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
print so.IsBalanced_Solution(root)
