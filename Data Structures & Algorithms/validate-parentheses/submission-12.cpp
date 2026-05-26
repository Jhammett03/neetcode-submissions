class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stk;
        std::unordered_map<char, char> mpg = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        for (char c : s) {
            if (mpg.contains(c)) {
                if (!stk.empty() && stk.top() == mpg[c]) {
                    stk.pop();
                } else {
                 return false;
                }
            }
            else {
                stk.push(c);
            }
        }
        return stk.empty();
    }
};
