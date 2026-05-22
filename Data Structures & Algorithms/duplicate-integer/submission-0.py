class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for x in nums:
            dic[x] = dic.get(x,0) + 1
            if dic[x]>=2:
                return True
        return False
