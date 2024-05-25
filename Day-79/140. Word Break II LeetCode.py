class Solution:
    def dfs(self, i, s, curr, res, wordDict):
        if i == len(s):
            res.append(" ".join(curr))
            return
        for j in range(i, len(s)):
            w = s[i : j + 1]
            if w in wordDict:
                curr.append(w)
                self.dfs(j+1, s, curr, res, wordDict)
                curr.pop()

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        curr = []
        res = []
        wordDict = set(wordDict)
        self.dfs(0, s, curr, res, wordDict)
        return res
