class Solution:
    def deleteK(self, head, k):
        if k == 0:
            return head
        if k == 1:
            return 
        x = head
        temp = 1
        while x.next:
            if not x.next.next and temp >= k - 1:
                x.next = None
                break
            if temp >= k - 1:
                x.next = x.next.next
                temp = 1
            else:
                temp += 1
            x = x.next
        return head

