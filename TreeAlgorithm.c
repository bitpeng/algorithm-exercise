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

