
class Solution:
    def check(self, mid, stations, k, n):
        count = 0
        for i in range(1, n):
            d = stations[i] - stations[i - 1]
            if d > mid:
                count += d // mid
        return count <= k
    
    def findSmallestMaxDist(self, stations, K):
        n = len(stations)
        l = 0.0
        h = 0.0
        for i in range(1, n):
            h = max(h, stations[i] - stations[i - 1])
        
        res = h
        limit = 10 ** -5
        while(h - l > limit):
            mid = (h - l) / 2.0 + l
            if self.check(mid, stations, K, n):
                h = mid
                res = mid
            else:
                l = mid
        return res
        
