class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(target, path, ind):
            if target==0:
                return result.append(path[:])
            if ind==len(nums):
                return
            if nums[ind]<=target:
                path.append(nums[ind])
                backtrack(target-nums[ind], path, ind)
                path.pop()
            backtrack(target, path, ind+1)
        backtrack(target , [], 0)
        return result
