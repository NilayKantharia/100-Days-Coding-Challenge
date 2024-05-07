# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        curr = head
        prev = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        reversed = self.reverse(head)
        x = reversed
        carry = 0
        prev = None
        while x:
            prev = x
            temp = x.val * 2 + carry
            x.val = temp % 10
            carry = temp // 10
            x = x.next
        
        while carry:
            prev.next = ListNode(carry % 10)
            carry //= 10
            prev = prev.next

        return self.reverse(reversed)
        
