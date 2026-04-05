class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if heights is None: 
            return 0

        l,r = 0, len(heights)-1
        largestArea = 0

        while l < r:
            currentArea = (r-l) * min(heights[l], heights[r])
            largestArea = max(largestArea, currentArea)
            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
        return largestArea