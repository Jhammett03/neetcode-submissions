class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mps = {}
        mpt = {}
        for i in range(len(s)):
            if s[i] in mps:
                mps[s[i]] += 1
            else:
                mps[s[i]] = 1
            if t[i] in mpt:
                mpt[t[i]] += 1
            else:
                mpt[t[i]] = 1
        return mps == mpt
