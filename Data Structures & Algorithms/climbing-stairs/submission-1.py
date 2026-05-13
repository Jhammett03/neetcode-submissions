class Solution:
    def climbStairs(self, n: int) -> int:
        l, r = 1, 1
        for i in range(n - 1):
            l, r = l + r, l
        return l