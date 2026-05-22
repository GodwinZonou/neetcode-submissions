class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        left, right = [1], [1]
        l, r = 1, 1
        for i in range(0,n-1):
            l *= nums[i]
            left.append(l)

        for i in range(n-1, 0, -1):
            r *= nums[i]
            right.append(r)
        
        for i in range(0,n):
            res.append(left[i]*right[n-i-1])
        
        return res

