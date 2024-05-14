from typing import List
import heapq


class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        minHeap =[[0, 0, 0]]
        visited = set()
        dirs = [[0, 1],[0, -1],[1, 0],[-1, 0]]
        
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            if (r, c) == (rows - 1, cols - 1):
                return diff
            visited.add((r, c))
            for nr, nc in dirs:
                newR = r + nr
                newC = c + nc
                
                if newR < 0 or newC < 0 or newR == rows or newC == cols or (newR, newC) in visited:
                    continue
                nd = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, (nd, newR, newC))
            
        
        
        
