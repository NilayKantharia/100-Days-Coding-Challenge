class Solution:
    def rev(self, head):
        if not head or not head.next: return head
        prev = None
        temp = head
        nextp = head.next
        
        while nextp:
            temp.next = prev
            prev = temp
            temp = nextp
            nextp = temp.next
        temp.next = prev
        return temp
        
    def addTwoLists(self, num1, num2):
        
        while num1.next and num1.data == 0:
            num1 = num1.next
        while num2.next and num2.data == 0:
            num2 = num2.next
        
        num1 = self.rev(num1)
        num2 = self.rev(num2)
        
        head = num1
        carry = 0
        while num1 and num2:
            num1.data += num2.data + carry
            carry = num1.data // 10
            num1.data %= 10
            tail = num1
            num1 = num1.next
            num2 = num2.next
            
        if num2:
            tail.next = num2
            num1 = num2
        
        while num1:
            num1.data += carry
            carry = num1.data // 10
            num1.data %= 10
            tail = num1
            num1 = num1.next
        
        num1 = tail
        while carry:
            num1.next = Node(carry)
            carry = num1.data // 10
            num1.data %= 10
            num1 = num1.next
            
        return self.rev(head)
