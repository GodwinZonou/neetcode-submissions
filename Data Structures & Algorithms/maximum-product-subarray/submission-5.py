class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        max_product = 1
        min_product = 1
        for x in nums:
            temp = max_product*x
            max_product = max(temp, min_product*x, x)
            min_product = min(temp, min_product*x, x)
            res = max(res, max_product)
        return res