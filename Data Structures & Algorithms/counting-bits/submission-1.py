class Solution:
    def countBits(self, n: int) -> List[int]:

        """ This approach is O(NlogN)
        ans = []
        def counting(number):
            count = 0
            while number:
                number = number&(number-1)
                count+=1
             return count
        for i in range(n+1):
            ans.append(counting(i))
        return ans """

        """
        This can be solved in O(N) using the kernighan's algorithm.
        key observation is the for any number (x), the number of one bits in x is equal to counting the number of one bits in x with its rightmost bit removed (y) plus 1
        the y is already solved before so we dont have to repeat the work, the observation that y is just one bit shorter than x so it must be smaller is trivial
        """
        dp = [0]*(n+1)
        for i in range(1,n+1):
            #Notice how in RHS, we are computing i&(i-1) which is equivalent to removing the rightmost bit
            dp[i] = dp[i&(i-1)] + 1
        return dp