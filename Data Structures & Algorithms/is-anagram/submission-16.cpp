class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        std::unordered_map<char, int> smap;
        std::unordered_map<char, int> tmap;

        for (int i = 0; i < s.size(); i++) {
            if (smap.contains(s[i])) {
                smap[s[i]]++;
            }
            else {
                smap[s[i]] = 1;
            }
            if (tmap.contains(t[i])) {
                tmap[t[i]]++;
            }
            else {
                tmap[t[i]] = 1;
            }
        }

        return smap == tmap;


    }
};
