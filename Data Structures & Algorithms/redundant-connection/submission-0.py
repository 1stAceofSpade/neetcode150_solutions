class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = [-1] * (len(edges) + 1)
        def find_root(n: int) -> int:
            if parent[n] == -1:
                return n
            parent[n] = find_root(parent[n])
            return parent[n]
        for u, v in edges:
            x = find_root(u)
            y = find_root(v)
            if x == y:
                return [u, v]
            
            parent[y] = x
        return []