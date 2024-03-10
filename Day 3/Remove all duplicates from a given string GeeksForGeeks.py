class Solution:
	def removeDuplicates(self,st):
	    s=set()
	    res=""
	    i=0
	    n=len(st)
	    while i<n:
            if not(str[i] in s):
                s.add(st[i])
                res+=st[i]
            i+=1
        return res
