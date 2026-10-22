class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def squares(num):
            tot = 0
            while num>0:
                dig = num%10
                tot += dig*dig
                num = num//10
            return tot
        while n not in seen:
            seen.add(n)
            n = squares(n)
            if n == 1:
                return True
        return False