class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        l, r = 0, len(heights) - 1

        while l < r :
            vol = (r - l) * min(heights[l], heights[r])
            if vol > max:
                max = vol
            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
        
        return max