/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
 
/*
    求二叉树是否是对称的！
*/ 
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root)
            return true;
        return Symmetric(root, root);
        
    }
    bool Symmetric(TreeNode* r1, TreeNode* r2)
    {
        if (!r1 && !r2)    // 均为空
            return true;    //否则肯定有一个非空！那么假如另一个为空时。
        else if (!r1 || !r2)
            return false;
        if (r1->val == r2->val)
            return Symmetric(r1->left, r2->right) && Symmetric(r1->right, r2->left);
        else return false;
    }    
};

// ============================================================================

/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

//  给定一个二叉树，找出其最小深度。
//  二叉树的最小深度为根节点到最近叶子节点的距离。
#include<limits.h>
class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: An integer
     */
    void PreOrder(TreeNode *root, std::vector<TreeNode*> &path)
    {
        if (!root)
            return;
        path.push_back(root);
        if(!root->left && !root->right)
            if (path.size() < min)
                min = path.size();
        if(root->left) PreOrder(root->left, path);
        if(root->right) PreOrder(root->right, path);
        path.pop_back();
    }
    int minDepth(TreeNode *root) {
        // write your code here
        if (!root)
            return 0;
        std::vector<TreeNode*> path;
        PreOrder(root, path); 
        return min;
    }
    Solution():min(INT_MAX){;}
private:
    int min;
};

// ============================================================================

//  判断树是不是合法的二叉排序数！

/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    bool isValidBST(TreeNode *root) {
        // write your code here
        if (!root)return true;
        std::stack<TreeNode*> st;
        int lastVal;
        bool firstAccess = true;
        while(root || !st.empty())
        {
            if (root)
            {
                st.push(root);
                root = root->left;
            }
            else
            {
                root = st.top();st.pop();
                if (firstAccess)
                {
                    lastVal = root->val;
                    firstAccess = false;
                }
                else
                    if (root->val > lastVal)
                        lastVal = root->val;
                    else return false;
                root = root->right;
            }
        }
        return true;
    }
};

// ============================================================================

// 判断两个数是不是相同的

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return Same(p, q);    
    }
    bool Same(TreeNode* r1, TreeNode* r2)
    {
        if (!r1 && !r2)    // 均为空
            return true;    //否则肯定有一个非空！那么假如另一个为空时。
        else if (!r1 || !r2)
            return false;
        if (r1->val == r2->val)
            return Same(r1->left, r2->left) && Same(r1->right, r2->right);
        else return false;
    }  
};


