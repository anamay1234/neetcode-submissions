# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My solution Done on Feb 14
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = head

        inc = 0
        # Getting Fast PTR to the Node we want to delete
        while inc < n:
            fast = fast.next
            inc += 1


        # Gets Slow PTR to one before the Node we want to delete
        while fast != None:
            slow = slow.next
            fast = fast.next 

        slow.next = slow.next.next

        return dummy.next

        