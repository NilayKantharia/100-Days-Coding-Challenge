class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = float('inf')

        pairs = []
        for i in range(len(quality)):
            pairs.append((wage[i] / quality[i], quality[i]))

        pairs.sort(key = lambda p : p[0])

        maxHeap = []
        total = 0
        for rate, q in pairs:
            heapq.heappush(maxHeap, -q)
            total += q

            if len(maxHeap) > k:
                total += heapq.heappop(maxHeap)
            if len(maxHeap) == k:
                res = min(res, total * rate) 
        
        return res

        
