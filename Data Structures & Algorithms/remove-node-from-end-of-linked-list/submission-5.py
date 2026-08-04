# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next

        # edge case if only one node
        if length == 1:
            head = None
            return head 

        # now we have length of LL
        distanceToNodeBefore = length - n
        i = 0
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while i < distanceToNodeBefore:
            curr = curr.next
            i += 1

        # Now adjust edges
        curr.next = curr.next.next
        return dummy.next

        

        