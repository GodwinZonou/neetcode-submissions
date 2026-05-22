class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount==0: 
                return 0
            if amount<0: 
                return -1
            if amount in memo:
                return memo[amount]
            res = float('inf')
            for c in coins:
                if c>amount:
                    continue
                if dfs(amount-c)==-1:
                    continue
                res = min(res, 1 + dfs(amount-c))
            memo[amount] = res
            return res if res!=float('inf') else -1
        return dfs(amount)