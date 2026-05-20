class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res = 0;
        int tot = 0;

        for (int i = 1; i < nums.size() + 1; i++){
            res += nums[i - 1];
            tot += i;
        }
        return tot - res;
    }
};
