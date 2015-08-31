# coding:utf-8
import copy

'''
    递归算法的本质是利用函数的调用栈进行，实际上我们可以自行使用栈来进行模拟，
    这样的算法空间复杂度为O(h)，h为二叉树的高度。
    
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

# 非递归前序遍历
def PreOrder_2(root):
    if not root:
        return None
    tmp = root; st = []
    path = []
    while tmp or st:
        if tmp:
            path.append(tmp.x)
            st.append(tmp)
            tmp = tmp.left
        else:
            tmp = st.pop()
            tmp = tmp.right

    return path

def PreOrder_3(root):
    if not root:
        return

    print "%d,"%root.x,
    PreOrder_3(root.left);PreOrder_3(root.right)

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

################################################################################

# 计算从根节点到某一节点的路径
def Path(root, node):
    if not root or not node:
        #return None
        return []
    path = []; ret = []
    GetPath(root, node, path, ret)
    return ret

def GetPath(root, node, path, ret):
    if not root:
        return
    #path.append(root.x)
    path.append(root)
    if node == root:
        #print path[:]
        ret.append(path[:])
        ret[:] = path[:]
        #ret = copy.deepcopy(path[:])
        return
    if root.left: GetPath(root.left, node, path, ret)
    if root.right: GetPath(root.right, node, path, ret)
    path.pop()

# ============================================================================ #
# 求到node的路径，非递归
# 这个算法不正确，还要参考相关资料
def Path2(root, node):
    if not root or not node:
        return
    st = []; path = []
    while root or st:
        if root:
            path.append(root.x)
            st.append(root)
            root = root.left
        else:
            root = st.pop()
            root = root.right
            path.pop()
        if root == node:
            # print "here"
            return path[:]

################################################################################
'''
    求二叉树中两个节点的最大距离
'''
def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


def MaxDistOfTwoNode(root):
    if not root:
        return -1

    leftMaxDist = MaxDistOfTwoNode(root.left)
    rightMaxDist = MaxDistOfTwoNode(root.right)
    maxLeftDistToRoot = height(root.left)
    maxRightDistToRoot = height(root.right)
    return max(max(leftMaxDist, rightMaxDist), maxLeftDistToRoot + maxRightDistToRoot)

# ============================================================================ #
# 求最远距离
# 返回这棵树两个节点的最远距离和树高度
def MaxDistOfTwoNode_2(root):
    if not root:
        return -1, 0  # 返回当前树两个节点的最远距离和树本身的高度
    leftMaxDistandHeight = MaxDistOfTwoNode_2(root.left)
    rightMaxDistandHeight = MaxDistOfTwoNode_2(root.right)
    height = max(leftMaxDistandHeight[1], rightMaxDistandHeight[1]) + 1
    distance = max(max(leftMaxDistandHeight[0], rightMaxDistandHeight[0]),
               leftMaxDistandHeight[1] + rightMaxDistandHeight[1])
    return distance, height
    #return max(leftMaxDistandHeight[0], rightMaxDistandHeight[0])

# ============================================================================ #
# 求最远距离
# 返回这棵树两个节点的最远距离和树高度
# 使用命名元组重写
from collections import namedtuple
Result = namedtuple('Result', 'dist height')
def MaxDistOfTwoNode_3(root):
    if not root:
        return Result(-1, 0)
        #return -1, 0  # 返回当前树两个节点的最远距离和树本身的高度
    left= MaxDistOfTwoNode_3(root.left)
    right= MaxDistOfTwoNode_3(root.right)
    height = max(left.height, right.height) + 1
    distance = max(max(left.dist, right.dist),
                   left.height + right.height)
    return Result(distance, height)
    #return max(leftMaxDistandHeight[0], rightMaxDistandHeight[0])

################################################################################
def NodeInTree(root, node):
    if not node:
        return True
    if not root:
        return False
    if root == node:
        # print 'xxxx'
        return True
    #ret = NodeInTree(root.left, node)
    #if not ret:
    #    ret = NodeInTree(root.right, node)
    #return ret
    return NodeInTree(root.left, node) or NodeInTree(root.right, node)

def CommonNode(root, n1, n2):
    if not root or not n1 or not n2:
        return None
    n1InLeft = NodeInTree(root.left, n1)
    n2InLeft = NodeInTree(root.left, n2)
    if n1InLeft and n2InLeft:
        return CommonNode(root.left, n1, n2)
    if not n1InLeft and not n2InLeft:
        return CommonNode(root.right, n1, n2)
    return root
# ============================================================================ #
def CommonNode_2(root, n1, n2):
    path_n1 = Path(root, n1)
    path_n2 = Path(root, n2)
    ret = None
    for i in zip(path_n1, path_n2):
        if i[0] == i[1]:
            ret = i[0]
    return ret
################################################################################

root = Node(1)
root.left = Node(2);root.right = Node(3)
root.left.left = Node(4); root.left.right = Node(5)
root.right.left = Node(6); root.right.right = Node(7)
root.left.left.right = Node(8); root.right.left.right = Node(9)
#print PreOrder(root)
#print PreOrder_2(root)
#PreOrder_3(root)
#print PostOrder(root)
#print InOrder(root)
#print Hierarchy(root)
#print Path(root, root.right.left)
#print Path2(root, root.right.left)
#print MaxDistOfTwoNode(root)
#print MaxDistOfTwoNode_2(root)
#print MaxDistOfTwoNode_3(root)
#ret = CommonNode(root, root.left.left, root.right.left)
#ret = CommonNode(root, root.left.left.right, root.left.right)
#ret = CommonNode(root, root.left.left.right.left, root.left.right)
ret = CommonNode_2(root, root.left.left, root.right.left)
#ret = CommonNode_2(root, root.left.left.right, root.left.right)
#ret = CommonNode_2(root, root.left.left.right.left, root.left.right)
if ret: print ret.x
else: print None
# print NodeInTree(root.left, root.left.left), NodeInTree(root.left, root.right.left)
# print root.left == root.left

'''树结构如下：

        1
      /   \
    2       3
  /   \   /   \
4      5  6    7
  \        \
   8        9

'''



''' 求树两个节点的最先公共祖先 '''
