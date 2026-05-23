class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def orderof(matrix):
            r , c = len(matrix) , len(matrix[0])
            return r , c
        r , c = orderof(matrix)
        def bounds(a , b):
            if matrix[a][b] < target or matrix[0][0]> target:
                return -1
            else:
                return 1
        check = bounds(r-1 , c-1)
        if check == -1:
            return False
        """def std_bs(matrix , x_new):
            lo , hi = 0 , y-1
            while lo<=hi:
                mid = (lo+hi)//2
                if matrix[x_new][mid] == target:
                    return 1
                elif matrix[x_new][mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return 0
        for x_new in range(x):
            res = std_bs(matrix , x_new)
            if res == 1:
                return True
        return False """
        r , c = len(matrix) , len(matrix[0])
        lo , hi = 0 , r*c - 1
        def bs_matrix(matrix , lo , hi):
            while lo<=hi:
                mid = (lo+hi)//2
                r_new = mid//c
                c_new = mid%c
                val = matrix[r_new][c_new]
                if val == target:
                    return True
                elif val > target:
                    hi = mid-1
                else:
                    lo = mid+1
            return False
        return bs_matrix(matrix , lo , hi)
            