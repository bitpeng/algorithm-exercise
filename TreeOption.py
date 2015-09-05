# coding:utf-8
import copy
from random import randint
from collections import deque

class Node(object):
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

################################################################################
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
''' 求二叉树中两个节点的最大距离 '''
def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1

'''
    参考网址：https://github.com/ldfaiztt/algorithms-3/blob/master/bop/3.8.md
    二叉树中节点的最大距离必定是两个叶子节点的距离。求某个子树的节点的最大距离，有三种情况：
    1.两个叶子节点都出现在左子树；2.两个叶子节点都出现在右子树；3.一个叶子节点在左子树，一个叶子节点
    在右子树。只要求得三种情况的最大值，结果就是这个子树的节点的最大距离。
    int find_max_len(Node *root);
    case 1: 两个叶子节点都出现在左子树。find_max_len(root->pLeft);
    case 2: 两个叶子节点都出现在右子树。find_max_len(root->pRight);
    case 3: 一个出现在左子树，一个出现在右子树。distance(root->pLeft) + distance(root->pRight) +2;
    其中，distance()计算子树中最远的叶子节点与根节点的距离，其实就是左子树的高度减1。
    参考C代码如下： //但是这个描述不完全正确
    struct Node {
        int data;
        Node *pLeft;
        Node *pRight;
    };
    // 计算树的高度
    int height(Node *root)
    {
        if(root == NULL) {
            return 0;
        }
        return max(height(root->pLeft), height(root->pRight)) + 1;
    }
    int find_max_len(Node *root)
    {
        if(root == NULL) {
            return 0;
        }
        int lmax = find_max_len(root->pLeft); // 左子树中的最大距离
        int rmax = find_max_len(root->pRight); // 右子树中的最大距离

        int lh = 0, rh = 0;
        if(root->pLeft) {
            // 左子树最远的叶子节点与根节点的距离
            lh = height(root->pLeft);
        }
        if(root->pRight) {
            // 右子树最远的叶子节点与根节点的距离
            rh = height(root->pRight);
        }
        return max(max(lmax, rmax), lh + rh);
    }
'''
def MaxDistOfTwoNode(root):
    if not root:
        return -1

    leftMaxDist = MaxDistOfTwoNode(root.left)
    rightMaxDist = MaxDistOfTwoNode(root.right)
    maxLeftDistToRoot = height(root.left)
    maxRightDistToRoot = height(root.right)
    return max(max(leftMaxDist, rightMaxDist), maxLeftDistToRoot + maxRightDistToRoot)

# ============================================================================ #
# 求最远距离的第二种方法
'''
    思路：发现了吗？在MaxDistOfTwoNode算法求最远距离中，它要和左子树、右子树的最远距离、还有左右子树
    的高度和进行比较，然而在遍历过程中，求高度和求最远距离是分别递归的，又重复。实际上，在递归的过程
    中，我们就可以求得当前树木的高度，所以可以进行重写这个函数，不仅仅返回最远距离，还返回当前子树的
    高度！
    参考网址：http://www.cnblogs.com/miloyip/archive/2010/02/25/binary_tree_distance.html
'''
# 这个返回这棵树两个节点的最远距离和树高度
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
# 求最远距离，使用命名元组重写，思路和第二种一样。
# 返回这棵树两个节点的最远距离和树高度
from collections import namedtuple
Result = namedtuple('Result', 'dist height')
def MaxDistOfTwoNode_3(root):
    if not root:
        return Result(-1, 0)  # 当只有一个节点时，高度为1,最远的两个节点距离为0; 因此可以
                              # 推出空树的高度为0, 最远两个节点距离为-1
    left= MaxDistOfTwoNode_3(root.left)
    right= MaxDistOfTwoNode_3(root.right)
    height = max(left.height, right.height) + 1
    distance = max(max(left.dist, right.dist),
                   left.height + right.height)  # 当最远距离在根节点两边时，最远距离实际上就是
                                                # 左右子树的高度和.如完全二叉树1, 2, 3. 最远距离为
                                                # 2，左右子树高度为1，和为2
    return Result(distance, height)
    #return max(leftMaxDistandHeight[0], rightMaxDistandHeight[0])

################################################################################
''' 求树两个节点的最先公共祖先 '''
def NodeInTree(root, node):
    '''判断节点在不在二叉树中'''
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
'''
    思路:判断两个节点在不在左(右)子树中，如果在，则递归处理左(右)子树；如果一个节点在左子树而另一
    个在右子树，则返回当前根节点既可！不过这种方法包含大量重复的递归
'''
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
# 思路：求每一个点到根节点的路径, 路径的最后一个相同节点就是最近公共最先
def CommonNode_2(root, n1, n2):
    path_n1 = Path(root, n1)
    path_n2 = Path(root, n2)
    ret = None
    for i in zip(path_n1, path_n2):
        if i[0] == i[1]:
            ret = i[0]
    return ret

################################################################################
# 求二叉树的所有路径
def GetAllPath(root):
    if not root:
        return []
    ret = []; path = []
    GetPathOfLeaf(root, path, ret)
    return ret

def IsLeaf(root):
    return root and root.left is None and root.right is None

def GetPathOfLeaf(root, path, ret):
    if not root:
        return
    path.append(root.x)
    if IsLeaf(root):
        ret.append(path[:])
    if root.left: GetPathOfLeaf(root.left, path, ret)
    if root.right: GetPathOfLeaf(root.right, path, ret)
    path.pop()

################################################################################
# 判断二叉树是不是完全二叉树
def CompleteBinaryTree(root):
    if not root:
        return True
    dq = deque(); leafBegin = False
    #if ValidNode(root):dq.append(root)
    dq.append(root)
    #while True:
    while len(dq) > 0:
        tmp = dq.popleft()
        if not ValidNode(tmp):return False
        if leafBegin:
            if IsLeaf(tmp):pass
            else: return False
        else:
            if tmp.left:
                dq.append(tmp.left)
            if tmp.right:
                dq.append(tmp.right)
        if not leafBegin:
            leafBegin = LeafAfterThisNode(tmp)
    return True

# 只有node节点的右子树为空，则node之后的所有节点均要为叶子节点
def LeafAfterThisNode(root):
    if root.right is None:
        return True

# 判断节点是不是合法的二叉树节点
# 当节点没有左子树而有右子树，节点是不合法的
def ValidNode(node):
    if not node:
        return True
    if node.left is None and node.right is not None: return False
    #if IsLeaf(node): return True
    return True

################################################################################
# 求二叉树第K层节点个数
def KDepthNodes(root, K):
    if not root or K < 1:
        return 0
    dq = deque()
    dq.append((root, 1))
    ret = 0
    while len(dq) > 0:
        tmp, depth = dq.popleft()
        if depth == K:
            ret += 1
        elif depth > K:
            break
        else:
            if tmp.left: dq.append((tmp.left, depth + 1))
            if tmp.right: dq.append((tmp.right, depth + 1))
    return ret

################################################################################
# 求二叉树搜索树的第K个节点
def KthNode(pRoot, k):
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
                return root
            k -= 1
            root = root.right

    return None

################################################################################
# 求二叉树是不是平衡二叉树！一次递归法避免重复递归。

def depth(root):
    if not root:return 0
    return max(depth(root.left),depth(root.right)) + 1
         
def DepthAdnisBalanced(root):
    if not root: return True, 0
    left = DepthAdnisBalanced(root.left)
    right = DepthAdnisBalanced(root.right)
    rootDepth = max(left[1], right[1]) + 1
    rootBalanced = True
    if not left[0] or not right[0]:
        rootBalanced = False
    if -1 <= left[1] - right[1] <= 1:pass
    else:rootBalanced = False
    return rootBalanced, rootDepth
    
 
class Solution:
    def isBalanced(self, root):
        #result = DepthAdnisBalanced()
        return DepthAdnisBalanced(root)[0]
        
################################################################################
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''
def IsLeaf(root):
    return root and not root.left and not root.right

def GetAllPath(root, path, ret):
    if(not root):
        return
    path.append(root.val)
    if IsLeaf(root):
        n = int(''.join([unicode(i) for i in path]))
        ret.append(n)
    if root.left:
        GetAllPath(root.left, path, ret)
    if root.right:
        GetAllPath(root.right, path, ret)
    path.pop()     

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = []
        path = []
        GetAllPath(root, path, ret)
        return sum(ret)



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
#ret = CommonNode_2(root, root.left.left, root.right.left)
#ret = CommonNode_2(root, root.left.left.right, root.left.right)
#ret = CommonNode_2(root, root.left.left.right.left, root.left.right)
#if ret: print ret.x
#else: print None
# print NodeInTree(root.left, root.left.left), NodeInTree(root.left, root.right.left)
# print root.left == root.left

#print GetAllPath(root)
#print CompleteBinaryTree(root)
#for i in [1,2,3,4,5]:
#    print KDepthNodes(root, i),
for i in range(10):
    tmp = KthNode(root, i)
    if tmp: print tmp.x, 
    else: print None, 

'''树结构如下：

        1
      /   \
    2       3
  /   \   /   \
4      5  6    7
  \        \
   8        9

'''

