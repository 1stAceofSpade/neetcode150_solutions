class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        size = len(temperatures)
        for i in range(size-1 , -1 , -1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if stack:
                res.append(stack[-1]-i)
            else:
                res.append(0)
            stack.append(i)
        res.reverse()
        return res