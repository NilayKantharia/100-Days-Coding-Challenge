class Solution:
    def countElements(self, a, b, n, query, q):
        res = []
        maxi = max(max(a),max(b))
        cs = [0]*(maxi + 1)
        for i in b:
            cs[i] += 1
        for i in range(1,len(cs)):
            cs[i] += cs[i - 1]
        for i in query:
            res.append(cs[a[i]])
        return res
