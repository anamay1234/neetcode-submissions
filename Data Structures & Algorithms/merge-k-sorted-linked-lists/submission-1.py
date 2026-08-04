# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None

                mergedLists.append(self.merge(list1, list2))

            lists = mergedLists

        return lists[0] if lists else None


    def merge(self, h1, h2):

        dummy = ListNode()
        dumHead = dummy

        # merges two sorted Lists
        while h1 is not None and h2 is not None:
            if h1.val <= h2.val:
                dumHead.next = h1
                dumHead = dumHead.next
                h1 = h1.next
            else:
                dumHead.next = h2
                dumHead = dumHead.next
                h2 = h2.next
        
        if h1 is None:
            dumHead.next = h2
        else:
            dumHead.next = h1
        
        return dummy.next

        




        