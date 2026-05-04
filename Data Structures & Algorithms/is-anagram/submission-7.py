class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap -> O(n)
        mpS = {}
        mpT = {}
        for c in s:
            if c in mpS:
                mpS[c] += 1
            else:
                mpS[c] = 1
        
        for c in t:
            if c in mpT:
                mpT[c] += 1
            else:
                mpT[c] = 1

        return mpT == mpS
