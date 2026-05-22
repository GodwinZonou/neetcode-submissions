class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        U = set()
        l= 0
        max_length = 0
        for r in range(0, n):
            while s[r] in U:
               U.remove(s[l])
               l+=1
            U.add(s[r])
            max_length = max(max_length, r-l+1)
        return max_length