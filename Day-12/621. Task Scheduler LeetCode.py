class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count=Counter(tasks)
        maxHeap=[-i for i in count.values()]
        heapq.heapify(maxHeap)
        t=0
        q=deque()
        while maxHeap or q:
            t+=1
            if maxHeap:
                c=heapq.heappop(maxHeap)+1
                if c:
                    q.append([c,t+n])
            if q and q[0][1]==t:
                heapq.heappush(maxHeap,q.popleft()[0])
        return t
        
