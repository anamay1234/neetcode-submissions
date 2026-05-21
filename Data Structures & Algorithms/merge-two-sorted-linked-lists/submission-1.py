# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        sortedLL = ListNode()
        headofSortedLL = sortedLL

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                sortedLL.val = list1.val
                newNode = ListNode()
                sortedLL.next = newNode
                sortedLL = sortedLL.next

                list1 = list1.next
            elif list1.val > list2.val:
                sortedLL.val = list2.val
                newNode = ListNode()
                sortedLL.next = newNode
                sortedLL = sortedLL.next

                list2 = list2.next

        if list1 is None and list2 is None:
            return list1
        
        if list1 == None:
            sortedLL.val = list2.val
            sortedLL.next = list2.next
        elif list2 == None:
            sortedLL.val = list1.val
            sortedLL.next = list1.next

        return headofSortedLL