"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        seen = {}
        def clone(node):
            if node in seen:
                return seen[node]
            cpy = Node(node.val)
            seen[node]=cpy
            for neigh in node.neighbors:
                cpy.neighbors.append(clone(neigh))
            return cpy
        return clone(node)