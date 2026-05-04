class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        maps = {}
        mapt = {}
        for i in range(len(s)):
            if s[i] in maps:
                maps[s[i]] += 1
            else:
                maps[s[i]] = 1
            if t[i] in mapt:
                mapt[t[i]] += 1
            else:
                mapt[t[i]] = 1
        if(maps == mapt):
            return True
        return False