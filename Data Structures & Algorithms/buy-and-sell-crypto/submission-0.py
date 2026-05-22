class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        n = len(prices)
        max_profit = 0
        while j<n:
            profit = prices[j] - prices[i]
            if profit<0:
                i=j
                j+=1
            else:
                max_profit = max(max_profit, profit)
                j+=1
        return max_profit