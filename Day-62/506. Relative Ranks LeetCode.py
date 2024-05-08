class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score, reverse=True)
        res = []
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rankMap = {}
        for i, s in enumerate(sortedScore):
            if i < 3:
                rankMap[s] = medals[i] 
            else:
                rankMap[swh] = str(i + 1) 
        for s in score:
            res.append(rankMap[s])
        return res
