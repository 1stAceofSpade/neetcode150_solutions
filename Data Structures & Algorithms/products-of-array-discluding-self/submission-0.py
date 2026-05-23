from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        prefix, suffix = 1, 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        for j in range(n-1 , -1 , -1):
            ans[j] *= suffix
            suffix *= nums[j]
        return ans