# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ind = 1
        cur = head
        mydic = {}
        while cur.next:
            mydic[ind] = cur
            cur = cur.next
            ind+=1
        nth = ind - n + 1
        if ind == 1 :
            return None
        if nth == 1:
            return head.next
        prev = mydic[nth-1]
        if prev is None:
            return head.next
        prev.next = prev.next.next
        return head
