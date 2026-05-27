class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n==1 and nums[0]==target: 
            return 0
        l, r = 0, n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid
        if nums[l]==target: 
            return l 
        else: return -1
        
