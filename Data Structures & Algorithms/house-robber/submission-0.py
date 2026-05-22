class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        # dp = [0]*n
        # dp[-1] = nums[-1]
        prev2 = nums[-1]
        # dp[-2] = max(nums[-2], nums[-1])
        prev1 = max(nums[-2], nums[-1])
        best = prev1
        for i in range(n-3, -1, -1):
            best = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = best
        return best