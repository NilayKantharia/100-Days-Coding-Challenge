class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        temp=str()
        tdir={}
        s1=set(s)
        for i in s:
            if i in s1:
                if i in tdir:
                    tdir[i]+=1
                else:
                    tdir.update({i:1})
        for i in order:
            if i in tdir:
                while tdir[i]:
                    temp+=i
                    tdir[i]-=1
        for i in tdir:
            while tdir[i]:
                temp+=i
                tdir[i]-=1
        return temp
