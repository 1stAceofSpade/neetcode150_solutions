"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """ Hashmap solution interleaving one late """
        cur = head
        hashmap = {}
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            hashmap[cur].next = hashmap.get(cur.next)
            hashmap[cur].random = hashmap.get(cur.random)
            cur = cur.next
        cur = head
        return hashmap.get(cur)