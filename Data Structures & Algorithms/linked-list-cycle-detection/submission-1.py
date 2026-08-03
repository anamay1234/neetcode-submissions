# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        prev = head
        curr = head

        while curr != None and curr.next != None:
            
            prev = prev.next
            curr = curr.next.next

            if prev == curr:
                return True

        return False
        