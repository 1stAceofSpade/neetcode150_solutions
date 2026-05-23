class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculated_time(piles , k):
            c = 0
            size = len(piles)
            for i in range(size):
                if piles[i]%k == 0:
                    c+= piles[i]/k
                else:
                    c+=piles[i]//k + 1
            return c
        l , r = 1 , max(piles)
        ans = max(piles)
        while l<=r:
            mid = (l+r)//2
            c = calculated_time(piles , mid)
            if c <= h:
                r = mid-1
                ans = min(ans , mid)
            else:
                l = mid + 1
        return ans
