# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        headA=list1
        headT=list2
        a1=a
        while a-1:
            headA=headA.next
            a-=1
        headB=headA.next
        headA.next=list2
        b=b-a1
        while b:
            headB=headB.next
            b-=1
        while headT.next:
            headT=headT.next
        headT.next=headB.next

        return list1
