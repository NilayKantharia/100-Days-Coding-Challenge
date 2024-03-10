# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        res=ListNode(0)
        x=res
        while l1 and l2:
            temp=(l1.val+l2.val+carry)
            carry=temp/10
            res.next=ListNode(temp%10)
            l1=l1.next
            l2=l2.next
            res=res.next
        while l1:
            temp=(l1.val+carry)
            carry=temp/10
            res.next=ListNode(temp%10)
            l1=l1.next
            res=res.next
        while l2:
            temp=(l2.val+carry)
            carry=temp/10
            res.next=ListNode(temp%10)
            l2=l2.next
            res=res.next
        if carry:
            res.next=ListNode(carry)
        return x.next
        
