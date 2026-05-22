class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = float('-inf')
        for x in nums:
            curSum = max(curSum + x, x)
            res = max(res, curSum)
        return res
            