class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2==1: return False
        target = s // 2
        n = len(nums)
        memo = {}
        def dfs(i, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target:
                return False
            if i == n:
                return False
            if (i, curr_sum)  in memo:
                return memo[(i, curr_sum)]
            take = dfs(i+1, curr_sum+nums[i])
            skip = dfs(i+1, curr_sum)
            memo[(i, curr_sum)] = take or skip
            return memo[(i, curr_sum)]
        return dfs(0,0)