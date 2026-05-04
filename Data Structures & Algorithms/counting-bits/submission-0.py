class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(num):
            tot = 0
            while num:
                num &= num - 1
                tot +=1
            return tot

        res = []
        for i in range(n + 1):
            res.append(count(i))
        return res