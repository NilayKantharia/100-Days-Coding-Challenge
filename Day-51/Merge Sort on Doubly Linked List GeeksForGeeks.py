class Solution():
    def merge(self, first, second):
        
        if not first: return second
        if not second: return first
        
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
            
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second
            
            
    def getMid(self, head):
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp
#Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self,head):
        if not head or not head.next: return head
    
        mid = self.getMid(head)
        
        head = self.sortDoubly(head)
        mid = self.sortDoubly(mid)

        
        return self.merge(head, mid)
