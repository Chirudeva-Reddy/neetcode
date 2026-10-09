# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None 
        while curr != None:
            #find the value of nextnode
            next_node = curr.next 
            #point curr.next to prev
            curr.next = prev
            #shift prev one step forward(to current)
            prev = curr 
            #shift current to the next node
            curr = next_node
        
        return prev
        
        