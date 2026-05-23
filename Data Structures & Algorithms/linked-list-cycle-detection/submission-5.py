# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        cur = dummy.next
        count = 0
        if head is None or head.next is None:
            return False
        while cur.next and cur.next.next:
            if cur.val <= cur.next.val and cur.next.val >= cur.next.next.val:
                count+=1
            if count == 5:
                return True
            cur = cur.next
        return False