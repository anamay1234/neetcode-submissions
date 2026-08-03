# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        h1 = list1
        h2 = list2

        dummy = ListNode()
        mergedList = dummy

        while h1 != None and h2 != None:
            if h1.val <= h2.val:
                mergedList.next = h1
                mergedList = h1
                h1 = h1.next
            else:
                mergedList.next = h2
                mergedList = h2
                h2 = h2.next

        if h1 is None:
            mergedList.next = h2
        else:
            mergedList.next = h1

        return dummy.next

                


        
        