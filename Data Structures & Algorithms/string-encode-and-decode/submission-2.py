class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "^" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            wrdlen = ""
            while s[i] != "^":
                wrdlen += s[i]
                i += 1
            wrdlen = int(wrdlen) + 1
            word = ""
            for j in range(1, wrdlen):
                word += s[i + j]
            i += wrdlen
            res.append(word)
        return res

