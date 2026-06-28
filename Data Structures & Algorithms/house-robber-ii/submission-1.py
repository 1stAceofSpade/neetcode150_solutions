class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0] , nums[1])
        def rob(start , end):
            dp = [0]*n
            dp[start] = nums[start]
            if start + 1 < end:
                dp[start + 1] = max(nums[start], nums[start + 1])
            for i in range(start+2 , end):
                if start + 1 < end:
                    dp[start + 1] = max(nums[start], nums[start + 1])
                dp[i] = max(nums[i] + dp[i-2] , dp[i-1])
            return dp[end-1]
        ans1 = rob(0 , n-1)
        ans2 = rob(1, n)
        return max(ans1 , ans2)