# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while stack or cur: 
            #deepen until you find min val and append to stack for backprop
            while cur:
                stack.append(cur)
                cur = cur.left
            #found min, for every pop we can decrement k
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            #try to search right tree
            cur = cur.right
        
        