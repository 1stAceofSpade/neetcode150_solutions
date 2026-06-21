class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row , col = len(board)-1 , len(board[0])-1
        def boarddfs(r , c , start):
            if start==len(word):
                return True
            if (
                r<0 or
                r>row or
                c<0 or
                c>col or
                board[r][c]!=word[start]
            ):
                return False

            visited = board[r][c]
            board[r][c] = "#"
            found = (
                boarddfs(r+1, c, start+1) or
                boarddfs(r, c+1, start+1) or
                boarddfs(r-1, c, start+1) or
                boarddfs(r, c-1, start+1)
            )
            board[r][c] = visited
            return found
        for i in range(row+1):
            for j in range(col+1):
                if boarddfs(i , j, 0):
                    return True
        return False
