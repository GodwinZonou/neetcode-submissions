class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSub = float('-inf')
        for x in nums:
            curSum = max(x, curSum+x)
            maxSub = max(maxSub, curSum)
        return maxSub
        
            