class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = defaultdict(list)
        for word in strs:
            mp = [0] * 26
            for c in word:
                mp[ord(c.lower()) - ord("a")] += 1
            mappings[tuple(mp)].append(word)
        return list(mappings.values())
            
                
