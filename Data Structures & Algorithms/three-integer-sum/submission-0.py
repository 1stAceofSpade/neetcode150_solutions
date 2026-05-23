from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        nums = sorted(nums)
        for i in range(size-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            out_fix = nums[i]
            l , r = i+1 , size-1
            while l<r:
                val = out_fix + nums[l] + nums[r]
                if val==0:
                    res.append([nums[i] , nums[l] , nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif val<0:
                    l+=1
                else:
                    r-=1
        return res