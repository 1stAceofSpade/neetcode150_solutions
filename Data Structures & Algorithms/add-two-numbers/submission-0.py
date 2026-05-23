# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur1 , cur2 = l1 , l2
        dummy = ListNode(0)
        tail = dummy
        while cur1 or cur2 or carry:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            tot = val1 + val2 + carry
            dig = tot%10
            carry = tot//10
            tail.next = ListNode(dig)
            tail = tail.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        return dummy.next