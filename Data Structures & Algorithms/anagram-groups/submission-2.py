class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            characters = [0]*26
            for c in s:
                characters[ord(c)-ord('a')] += 1
            dic[tuple(characters)].append(s)
        print(dic)
        return list(dic.values())

        
            


