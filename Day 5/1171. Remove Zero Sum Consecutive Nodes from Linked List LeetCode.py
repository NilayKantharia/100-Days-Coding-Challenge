# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dictionary={}
        sums=0
        duplicate_head=ListNode(0,head) 
        temp=duplicate_head 
        while temp:
            sums+=temp.val
            dictionary[sums]=temp
            temp=temp.next
        sums=0
        temp=duplicate_head
        while temp:
            sums+=temp.val
            temp.next=dictionary[sums].next
            temp=temp.next
        return duplicate_head.next
