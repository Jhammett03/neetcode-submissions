# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.deepen(root, float('inf'), float('-inf'))
   
    def deepen(self, root, upper, lower):
        if not root: return True
        if not (lower < root.val < upper): return False
        return self.deepen(root.left, root.val, lower) and self.deepen(root.right, upper, root.val)