class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i != j and i != k and j != k:
                        arr = [nums[i], nums[j], nums[k]]
                        arr.sort()
                        if nums[i] + nums[j] + nums[k] == 0 and arr not in res:
                            res.append(arr)
        return res