# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, current = None, head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev