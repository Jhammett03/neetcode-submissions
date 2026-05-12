class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sset = {}
        tset = {}

        for i in range(len(s)):
            sset[s[i]] = sset.get(s[i], 0) + 1
            tset[t[i]] = tset.get(t[i], 0) + 1
        return sset == tset