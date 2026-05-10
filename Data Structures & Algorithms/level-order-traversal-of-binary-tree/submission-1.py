# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        if not root: return res

        while len(q) > 0:
            levelcnt = len(q)
            sub = []

            for _ in range(levelcnt):
                cur = q.popleft()
                sub.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(sub)
        return res