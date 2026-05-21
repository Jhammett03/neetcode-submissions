class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> mapping = {
            {')', '('},
            {']', '['},
            {'}', '{'}  
        };
        std::stack<char> stk;

        for (char c : s) {
            if (mapping.contains(c)) {
                if (stk.empty() || stk.top() != mapping[c]) return false;
                stk.pop();
            }
            else {
                stk.push(c);
            }
        }

        return stk.empty();
        
    }
};
