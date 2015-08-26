# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, K):
        # write code here
        if not pRoot or K <= 0:
            return None
        cnt = 0
        result = None
        return self.Inorder(pRoot, cnt, K, result)

    def Inorder(self, pRoot, cnt, K, result):
        if not pRoot:
            return
        self.Inorder(pRoot.left, cnt, K, result)
        #print pRoot.val
        cnt += 1
        #print cnt, K
        if cnt == K:
            result = root
            return
            #print pRoot.val
            #return pRoot.val
        self.Inorder(pRoot.right, cnt, K, result)



root = TreeNode(8)
root.left = TreeNode(6);root.right = TreeNode(10)
root.left.left = TreeNode(5);root.left.right = TreeNode(7)
so = Solution()
print so.KthNode(root, 1).val
print so.KthNode(root, 2).val
print so.KthNode(root, 3).val
print so.KthNode(root, 4).val
print so.KthNode(root, 5).val
#print so.KthNode(root, 6).val
#print so.KthNode(root, -1).val
#print so.KthNode(root, 8).val
