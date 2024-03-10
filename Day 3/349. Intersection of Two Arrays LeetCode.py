class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1=len(nums1)-1
        l2=len(nums2)-1
        s=set()
        res=set()
        i=0;j=0
        s.update(nums1)
        for i in range(l2+1):
            if nums2[i] in s:
                res.add(nums2[i])
        return list(res)
        
            
        
