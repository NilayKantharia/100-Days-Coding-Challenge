class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        res=len(points)
        p=points[0]
        print(points)
        for i in range(1,len(points)):
            c=points[i]
            if c[0]<=p[1]:
                res-=1
                p=[c[0],min(p[1],c[1])]
            else:
                p=c
        return res
        
