class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2: return max(nums)
        
        def rob_linear(nums):
            n = len(nums)
            if n==1: return nums[0]
            prev1 = max(nums[-1], nums[-2])
            prev2 = nums[-1]
            best = prev1
            for i in range(n-3, -1, -1):
                best = max(nums[i] + prev2, prev1)
                prev2 = prev1
                prev1 = best
            return best
        
        m1 = rob_linear(nums[:-1])
        m2 = rob_linear(nums[1:])
        return max(m1, m2)