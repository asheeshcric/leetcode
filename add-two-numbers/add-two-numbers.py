# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convert_to_number(self, head):
        number = ""
        while head is not None:
            number += str(head.val)
            head = head.next
            
        return int(number[::-1])
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.convert_to_number(l1)
        num2 = self.convert_to_number(l2)
        result = num1 + num2
        num = str(result)[::-1]
        head = ListNode(val=int(num[0]))
        node = head
        for digit in num[1:]:
            node.next = ListNode(int(digit))
            node = node.next
        
        return head
        
            
        
        