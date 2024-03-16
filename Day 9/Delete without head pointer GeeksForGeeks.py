class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,del_node):
        del_node.data,del_node.next.data=del_node.next.data,del_node.data
        if del_node.next.next:
            del_node.next=del_node.next.next
        else:
            del_node.next=None
            
