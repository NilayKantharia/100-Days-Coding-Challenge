# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        t = ListNode(head.val,None)
        head = head.next
        while head:
            t = ListNode(head.val,t)
            head = head.next
        return t
