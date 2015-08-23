# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []

        ret = []
        path = []
        self.Find(root, expectNumber, ret, path)
        print ret
        a = [];self.f(a);print a
        return ret

    def f(self, a):
        a.append(1)


    def Find(self, root, target, ret, path):
        if not root:
            return

        path.append(root.val)
        isLeaf = (root.left is None and root.right is None)
        if isLeaf and target == root.val:
            ret.append(path[:])   # 这里这一步要千万注意啊，
            #ret.append(path)   # 这里这一步要千万注意啊，
            # 假如是:ret.append(path), 结果是错的。因为Python可变对象都是引用传递啊。

        print "target:", target, "isLeaf:", isLeaf,
        print "val:", root.val, "path:", path, "ret:", ret
        print

        if root.left:
            self.Find(root.left, target - root.val, ret, path)
        if root.right:
            self.Find(root.right, target - root.val, ret, path)

        path.pop()


so = Solution()
Tree = TreeNode(1)
Tree.left = TreeNode(3)
Tree.left.left = TreeNode(3)
Tree.right = TreeNode(6)
print so.FindPath(Tree, 7)
