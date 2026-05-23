class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def orderof(matrix):
            a , b = len(matrix) , len(matrix[0])
            return a , b
        x , y = orderof(matrix)
        def bounds(a , b):
            if matrix[a][b] < target or matrix[0][0]> target:
                return -1
            else:
                return 1
        check = bounds(x-1 , y-1)
        if check == -1:
            return False
        def std_bs(matrix , x_new):
            lo , hi = 0 , y-1
            while lo<=hi:
                mid = (lo+hi)//2
                if matrix[x_new][mid] == target:
                    return 1
                elif matrix[x_new][mid] < target:
                    lo +=1
                else:
                    hi -=1
            return 0
        for x_new in range(x):
            res = std_bs(matrix , x_new)
            if res == 1:
                return True
        return False