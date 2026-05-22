class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occurence = set(nums)
        start = {}
        for x in nums:
            if x-1 not in occurence:
                start[x] = 1
        max_length = 0
        for x in start:
            next_number = x+1
            while next_number in occurence:
                start[x] += 1
                next_number += 1
            max_length = max(max_length, start[x])
        return max_length
            
        
