class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
        m , n = len(heights) , len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r , c , visited , prev_h):
            if (
                r<0 or
                r>=m or
                c<0 or
                c>=n or
                (r , c) in visited or
                prev_h>heights[r][c]
            ):
                return
            visited.add((r , c))
            dfs(r-1 , c, visited, heights[r][c])
            dfs(r , c-1, visited, heights[r][c])
            dfs(r , c+1 , visited , heights[r][c])
            dfs(r+1 , c , visited , heights[r][c])
        for i in range(m):
            dfs(i , 0 , pacific , heights[i][0])
            dfs(i , n-1 , atlantic , heights[i][n-1])
        for j in range(n):
            dfs(0 , j , pacific , heights[0][j])
            dfs(m-1 , j , atlantic , heights[m-1][j])
        res = [[r , c] for r , c in pacific & atlantic]
        return res