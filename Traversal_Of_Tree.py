# coding:utf-8

'''
递归算法的本质是利用函数的调用栈进行，实际上我们可以自行使用栈来进行模拟，这样的算法空间复杂度为O(h)，h为二叉树的高度。

前序遍历
首先把根节点入栈，然后在每次循环中执行以下操作：
此时栈顶元素即为当前的根节点，弹出并打印当前的根节点。
把当前根节点的右儿子和左儿子分别入栈（注意是右儿子先入栈左儿子后入栈，这样的话下次出栈的元素才是左儿子，
这样才符合前序遍历的顺序要求：根节点->左儿子->右儿子）。
下面是代码实现。


后序遍历
因为后序遍历的顺序是：左子树->右子树->根节点，于是我们在前序遍历的代码中，当访问完当前节点后，先把当
前节点的左子树入栈，再把右子树入栈，这样最终得到的顺序为：根节点->右子树->左子树，刚好是后序遍历倒过
来的版本，于是把这个结果做一次翻转即为真正的后序遍历。而翻转可以通过使用另外一个栈简单完成，这样的代
价是需要两个栈，但就复杂度而言，空间复杂度仍然是O(h)。


中序遍历
中序遍历稍微复杂，使用一个指针p指向下一个待访问的节点，p初始化为根节点。在每次循环中执行以下操作：
如果p非空，则把p入栈，p变为p的左儿子。
如果p为空，说明已经向左走到尽头了，弹出当前栈顶元素，进行访问，并把p更新为其右儿子。
'''
from random import randint

class Node(object):
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

def PreOrder(root):
    if not root:
        return None
    st = [root]    # 辅助栈
    path = []      # 遍历路径
    while st:
        node = st.pop()
        path.append(node.x)
        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)
    return path

def PostOrder(root):
    if not root:
        return None
    st = [root]
    path = []
    while st:
        node = st.pop()
        path.append(node.x)
        if node.left:
            st.append(node.left)
        if node.right:
            st.append(node.right)
    return path[::-1] # path值为：根节点->右子树->左子树，所以作一次倒序刚好就是返回结果！

def InOrder(root):
    if not root:
        return None
    tmp = root; st = []
    path = []
    while tmp or st:
        if tmp:
            st.append(tmp)
            tmp = tmp.left
        else:
            tmp = st.pop()
            path.append(tmp.x)
            tmp = tmp.right

    return path

def Hierarchy(root):
    # write code here
    from collections import deque
    #if root is None:
    #    return None
    if not root:
        return []

    q = deque()
    q.append(root)
    ret = []
    while len(q) > 0:
        node = q.popleft()
        ret.append(node.x)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        #q.append(node.right) if node.right else pass
    return ret

root = Node(1)
root.left = Node(2);root.right = Node(3)
root.left.left = Node(4); root.left.right = Node(5)
root.right.left = Node(6); root.right.right = Node(7)
root.left.left.right = Node(8); root.right.left.right = Node(9)
print PreOrder(root)
print PostOrder(root)
print InOrder(root)
print Hierarchy(root)

'''树结构如下：

        1
      /   \
    2       3
  /   \   /   \
4      5  6    7
  \        \
   8        9

'''



