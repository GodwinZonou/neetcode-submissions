class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n!=m: return False

        dic1, dic2 = {}, {}
        for c1,c2 in zip(s,t):
            dic1[c1] = dic1.get(c1,0) + 1
            dic2[c2] = dic2.get(c2,0) + 1
        return dic1==dic2
            
