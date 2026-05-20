class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        std::unordered_map<char,int> counts;

        for (char c : s){
            counts[c] += 1;
        }

        for (char c : t) {
            counts[c] -= 1;
            if (counts[c] < 0) {
                return false;
            }
        }

        return true;
    }
};
