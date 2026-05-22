class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def freq(ch):
            dic={}
            for c in ch:
                dic[c] = 1 + dic.get(c,0)
            return dic
        freq1 = freq(s1)
        freq2 = {}
        l=0
        for r in range(len(s2)):
            freq2[s2[r]] = 1 + freq2.get(s2[r], 0)
            while (r-l+1)>len(s1):
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l+=1
            if freq1 == freq2:
                return True
        return False
