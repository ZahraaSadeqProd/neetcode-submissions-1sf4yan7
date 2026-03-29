# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) < 1:
            return None
        elif len(lists) < 2:
            return lists[0]

        dummy = ListNode(0, lists[0])

        for i in range(1, len(lists)):
            cur = lists[i]
            dummy = self.mergeSortList(dummy, cur)

        return dummy.next


    def mergeSortList(self, dummy, cur):
        tail = dummy
        list1 = dummy.next
        list2 = cur

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy

