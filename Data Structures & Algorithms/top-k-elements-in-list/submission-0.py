class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dic = {}
        n = len(nums)
        for x in nums:
            dic[x] = dic.get(x,0) +1
        freq = defaultdict(list)
        for x in dic:
            freq[dic[x]].append(x)
        for i in range(n, 0, -1):
            if i not in freq:
                continue
            j=0
            while j<len(freq[i]) and len(res)<k:
                res.append(freq[i][j])
                j+=1
            if len(res)>=k:
                break
        return res



