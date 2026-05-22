class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)
        n = len(s)
        def dfs(i):
            if i>=n:
                return True
            if i in memo:
                return memo[i]
            for j in range(i+1, n+1):
                if s[i:j] in wordSet and dfs(j):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return memo[i]
        return dfs(0)
        

