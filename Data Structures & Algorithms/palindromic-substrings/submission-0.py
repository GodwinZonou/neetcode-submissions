class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(left, right):
            cpt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cpt += 1
                left -= 1
                right += 1
            return cpt
        res = 0
        for i in range(len(s)):
            odd = expandAroundCenter(i,i)
            even = expandAroundCenter(i, i+1)
            res += odd + even
        return res
