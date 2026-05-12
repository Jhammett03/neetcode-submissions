class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            mp = [0] * 26
            for c in word:
                mp[ord(c) - ord("a")] += 1
            groups[tuple(mp)].append(word)
        return list(groups.values())
