class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
        temp1 = head1 if min(n1,n2)==n1 else head2
        hashSet = set()
        while temp1:
            hashSet.add(temp1.data)
            temp1=temp1.next
        
        res=0
        temp2 = head2 if max(n1,n2)==n2 else head1
        while temp2:
            sub=x-temp2.data
            if sub in hashSet:
                res+=1
            temp2=temp2.next
        return res
