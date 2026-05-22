class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def dfs(i):
            if i>=n:
                return 1
            if i in memo:
                return memo[i]
            res = 1
            for j in range(i+1, n):
                if nums[j]<=nums[i]:
                    continue
                res = max(res, 1+dfs(j))
            memo[i] = res
            return res
        return max(dfs(i) for i in range(n))
            