# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newListHead = None
        curr = head

        while curr != None:
            node = ListNode(curr.val, newListHead)
            newListHead = node

            curr = curr.next

        return newListHead
