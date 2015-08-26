# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k <= 0:
            return None

        stack = []; root = pRoot
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) > 0:
                root = stack.pop()
                #k -= 1
                if k == 1:
                    return root.val
                k -= 1
                root = root.right

        return None


root = TreeNode(8)
root.left = TreeNode(6);root.right = TreeNode(10)
root.left.left = TreeNode(5);root.left.right = TreeNode(7)
so = Solution()
print so.KthNode(root, 1)
print so.KthNode(root, 2)
print so.KthNode(root, 3)
print so.KthNode(root, 4)
print so.KthNode(root, 5)
print so.KthNode(root, 6)
print so.KthNode(root, -1)
print so.KthNode(root, 8)
