class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        m = float("inf")
        cpt = 0
        while l<r:
            mid = l + (r-l)//2
            if nums[mid]<nums[r]:
                r = mid
            elif nums[mid]>nums[r]:
                l = mid+1
        return nums[l]
            
            