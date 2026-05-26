class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def nextstep(ind):
            nxtind = nums[ind]
            return nxtind
        slow = nextstep(0)
        fast = nextstep(nextstep(0))
        while slow != fast:
            slow = nextstep(slow)
            fast = nextstep(nextstep(fast))
        loopptr = slow
        startptr = 0
        # notes: according to floyd distance from start to entrance of cycle is equal to distance from meeting point to entrance of cycle. so if both pointers move at same speed 1 step at a time then they will meet at start of the cycle
        while loopptr!=startptr:
            loopptr = nextstep(loopptr)
            startptr = nextstep(startptr)
        
        return loopptr