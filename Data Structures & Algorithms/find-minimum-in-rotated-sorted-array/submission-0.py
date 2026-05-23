class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums)-1
        while l<r:
            mid = (l+r)//2
            val = nums[mid]
            if val > nums[r]:
                l = mid+1
            else:
                r = mid
        return min(nums[l] , nums[r])