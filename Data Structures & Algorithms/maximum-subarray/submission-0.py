class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        curr = 0
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            max_total = max(curr, max_total)
        return max_total