class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sset = {}
        tset = {}
        for i in range(len(s)):
            if s[i] in sset:
                sset[s[i]] += 1
            else: sset[s[i]] = 1
            if t[i] in tset:
                tset[t[i]] += 1
            else: tset[t[i]] = 1
        return sset == tset
