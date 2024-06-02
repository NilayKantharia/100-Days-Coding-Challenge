class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        res = []
        temp = 0
        for i,j in reversed(queries):
            if i == 0:
                res.append(j ^ temp)
            else:
                temp ^= j
        res.append(0^temp)
        res.sort()
        return res
