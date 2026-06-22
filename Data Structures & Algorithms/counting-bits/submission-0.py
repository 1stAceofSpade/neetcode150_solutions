class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        def counting(number):
            count = 0
            while number:
                number = number&(number-1)
                count+=1
            return count
        for i in range(n+1):
            ans.append(counting(i))
        return ans