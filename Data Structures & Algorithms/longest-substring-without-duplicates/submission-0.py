class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r, tot = 0, 0, 0
        maxtot = 0

        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                tot -= 1
                l += 1
            else:
                seen.add(s[r])
                tot += 1
                maxtot = max(maxtot, tot)
                r += 1
        return maxtot


