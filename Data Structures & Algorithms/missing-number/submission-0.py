class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        size = len(nums)
        for i in range(size):
            ans = ans^i
            ans = ans^nums[i]
        return ans