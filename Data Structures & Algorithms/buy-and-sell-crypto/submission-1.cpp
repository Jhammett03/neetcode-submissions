class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;

        int curmin = prices[0];

        for (int n : prices) {
            if (n < curmin) {
                curmin = n;
            }
            else {
                max = std::max(n - curmin, max);
            }
        }
        return max;
    }
};
