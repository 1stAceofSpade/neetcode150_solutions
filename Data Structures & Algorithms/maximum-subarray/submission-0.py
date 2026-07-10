class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum , res = 0 , nums[0]
        for i in range(len(nums)):
            cursum=max(nums[i] , cursum+nums[i])
            res=max(res , cursum)

        return res