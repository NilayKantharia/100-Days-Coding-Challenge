# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3=ListNode()
        l=list3
        if not (list1 or list2):
            return
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            while list1 and list2:
                if list1.val<list2.val:
                    list3.next=ListNode(list1.val)
                    list3=list3.next
                    list1=list1.next
                elif list2.val<list1.val:
                    list3.next=ListNode(list2.val)
                    list3=list3.next
                    list2=list2.next
                else:
                    list3.next=ListNode(list1.val)
                    list3=list3.next
                    list3.next=ListNode(list2.val)
                    list3=list3.next
                    list1=list1.next
                    list2=list2.next
            if list1:
                list3.next=ListNode(list1.val,list1.next)
            if list2:
                list3.next=ListNode(list2.val,list2.next)
        return l.next
