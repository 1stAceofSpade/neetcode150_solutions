class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(ind , path):
            if ind == len(nums):
                result.append(path[:])
                return

            path.append(nums[ind])
            backtrack(ind+1 , path)
            path.pop()
            backtrack(ind+1 , path)
        backtrack(0 , [])
        return result