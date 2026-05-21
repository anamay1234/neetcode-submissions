# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # Getting slow->next to be the start of the 2nd half in the Linked List
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # curr is the the start of the 2nd part of the list
        prev = None
        curr = slow.next

        #seperated the two halfs of the Linked Lists
        slow.next = None

        #reverse the 2nd half of the list
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Now prev is the start of the 2nd half of the list, head is start of 1st half
        list1 = True

        while prev is not None:
            if list1:
                temp = head.next
                head.next = prev
                head = temp
                list1 = False
            else:
                temp = prev.next
                prev.next = head
                prev = temp
                list1 = True





        

        