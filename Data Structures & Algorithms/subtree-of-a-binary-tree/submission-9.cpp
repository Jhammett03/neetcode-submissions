/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root) return false;
        if (root->val == subRoot->val and sameTree(root, subRoot)) return true;
        return isSubtree(root->left, subRoot) or isSubtree(root->right, subRoot);
        
    }

    bool sameTree(TreeNode* p, TreeNode* q) {
        if (!p and !q) return true;
        if (!p or !q or p->val != q->val) return false;

        return sameTree(p->left, q->left) and sameTree(p->right, q->right);
    }
};
