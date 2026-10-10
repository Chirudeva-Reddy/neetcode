# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #creating a dummy node
        head = ListNode()
        tail = head

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                tail.next = list1
                #updating list1 pointer
                list1 = list1.next
            else:
                tail.next = list2
                #updating list2 pointer
                list2 = list2.next

            #tail pointer is updated regardless of which condition we follow
            tail = tail.next

        #inserting the entire remaining part of the list, cuz either list1 or list2 would be empty
        if list1 is not None:
            tail.next = list1
        if list2 is not None:
            tail.next = list2
            
        return head.next
