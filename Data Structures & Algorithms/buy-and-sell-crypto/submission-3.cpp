class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        int max = 0;

        int curmin = prices[0];

        for (const int n : prices) {
            curmin = std::min(curmin, n);
            max = std::max(n - curmin, max);

        }
        return max;
    }
};
