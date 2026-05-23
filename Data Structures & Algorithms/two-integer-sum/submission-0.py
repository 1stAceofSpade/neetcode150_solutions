class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in seen:
                if seen[target - nums[i]] > i:
                    return [i , seen[target - nums[i]]]
                else:
                    return [seen[target - nums[i]], i]
            else:
                seen[nums[i]] = i