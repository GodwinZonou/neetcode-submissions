class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i,j = 0, n-1
        max_water = 0
        while i<j:
            h = min(heights[i], heights[j])
            max_water = max(max_water, h*(j-i))
            if h==heights[i]:
                i+=1
            else:
                j-=1
        return max_water

