class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}
        for l in s:
            if l in maps:
                maps[l] += 1
            else:
                maps[l] = 1
        for l in t:
            if l in mapt:
                mapt[l] += 1
            else:
                mapt[l] = 1
        if(maps == mapt):
            return True
        return False