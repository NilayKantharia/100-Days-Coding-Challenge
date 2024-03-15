class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:
    def sort(self, h1):
        #return head
        res=Node(0)
        rr=res
        alt=0
        l=[]
        ll=res
        while h1:
            if not alt:
                res.next=Node(h1.data)
                res=res.next
                alt=1
            else:
                l.append(h1.data)
                alt=0
            h1=h1.next
        i=len(l)-1
        while i and ll.next:
            if ll.next and ll.data<=l[i]:
                ll=ll.next
            else:
                l[i],ll.data=ll.data,l[i]
            i-=1
        while ll.next:
            ll=ll.next
        n=len(l)
        for i in range(n-1,-1,-1):
            res.next=Node(l[i])
            res=res.next
        return rr.next
