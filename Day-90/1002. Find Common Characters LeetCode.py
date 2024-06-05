class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])

        for w in words:
            curr = Counter(w)

            for i in cnt:
                cnt[i] = min(cnt[i], curr[i])
        res = []
        for i in cnt:
            for j in range(cnt[i]):
                res.append(i)
        return res
