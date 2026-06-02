class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        left, right = 1, m
        k = left + (right-left)//2
        while left<right:
            hours = 0
            for pile in piles:
                q = pile//k
                r = pile%k
                hours += q
                if r>0:
                    hours += 1
            if hours>h:
                left = k+1
                k = left + (right-left)//2
            if hours<=h:
                right = k
                k = left + (right-left)//2
        return left
            


                
            