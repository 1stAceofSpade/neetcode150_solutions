class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        seen = {i:0 for i in range(n)}
        for u , v in edges:
            seen[u]+=1
            seen[v]+=1
        parent = [-1]*n
        def find(n):
            if parent[n]==-1:
                return n
            parent[n] = find(parent[n])
            return parent[n]
        for u , v in edges:
            x = find(u)
            y = find(v)
            if (x==y):
                return False
            parent[y]=x
        return True
