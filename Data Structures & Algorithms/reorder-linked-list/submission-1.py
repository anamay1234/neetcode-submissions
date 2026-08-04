# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = head
        curr = head
        
        while curr.next is not None:
            curr = curr.next.next
            if curr is None:
                break
            prev = prev.next
        
        # now prev at end of first LL
        curr = prev.next
        prev.next = None

        # Now we use temp reverse the 2nd part of the LL
        prev = None

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        
        # 2nd part is reversed and prev = head of 2nd part
        h1 = head
        h2 = prev

        while h1 is not None and h2 is not None:
            temp = h1.next
            h1.next = h2
            h1 = temp

            temp = h2.next
            h2.next = h1
            h2 = temp
        
        
        


