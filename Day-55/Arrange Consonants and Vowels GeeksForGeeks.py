class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        if not head or not head.next:
            return head

        x = head
        conso = 0
        length = 0
        vow = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        while x:
            if x.data not in vowels:
                conso += 1
            else:
                vow += 1
            length += 1
            tail = x
            x = x.next
            
        if not conso or not vow:
            return head
            
        x = head
        while x.data not in vowels:
            head = head.next
            temp = x
            x = x.next
            temp.next = None
            tail.next = temp
            tail = tail.next
            conso -= 1
            
        temp = head.next
        prev = head
        while temp.next and conso:
            if temp.data not in vowels:
                prev.next = temp.next
                tail.next = temp
                temp.next = None
                tail = temp
                temp = prev.next
                conso -= 1
            else:
                prev = temp
                temp = temp.next
        
        
        return head
