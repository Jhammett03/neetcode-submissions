class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;
        seen.reserve(nums.size());

        for (int i = 0; i < nums.size(); i++){
            if (seen.contains(nums[i])) {
                return true;
            }
            seen.insert(nums[i]);
        }
        return false;
    }
};