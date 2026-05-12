class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l, r = 0, len(heights) - 1
        while l < r:
            height = (r-l) * min(heights[l], heights[r])
            m = max(m,height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return m