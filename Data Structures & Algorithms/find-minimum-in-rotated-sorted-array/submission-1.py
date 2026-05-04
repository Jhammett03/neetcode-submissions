class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        if mid-1 >= 0 and nums[mid - 1] > nums[mid]:
            return nums[mid]
        else:
            #binary search
            if nums[mid] > nums[len(nums) - 1]:
                return self.findMin(nums[mid:])
            else:
                return self.findMin(nums[:mid])
