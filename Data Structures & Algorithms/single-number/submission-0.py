class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        start = nums[0]
        size = len(nums)
        for i in range(1 , size):
            start=start^nums[i]
        return start