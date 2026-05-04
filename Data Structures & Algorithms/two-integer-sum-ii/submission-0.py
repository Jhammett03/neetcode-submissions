class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in m:
                return [m[complement] + 1, i + 1]
            m[numbers[i]] = i
        return []