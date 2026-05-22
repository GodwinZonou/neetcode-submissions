class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array = sorted(nums)
        n = len(nums)
        res = []
        i = 0
        while i<n:
            if sorted_array[i]>0:
                break
            target = - sorted_array[i]
            dic = {}
            j, k = i+1, n-1
            while j<k:
                s = sorted_array[j] + sorted_array[k]
                if s<target:
                    j+=1
                elif s>target:
                    k-=1
                else:
                    res.append(tuple([sorted_array[i], sorted_array[j], sorted_array[k]]))
                    j+=1
                    k-=1
            i+=1

        return list(set(res))
                


