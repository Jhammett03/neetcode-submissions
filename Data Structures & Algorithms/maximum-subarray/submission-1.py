class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxtot = nums[0]
        curr = 0
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            maxtot = max(maxtot, curr)
        return maxtot