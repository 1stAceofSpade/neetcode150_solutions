from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        mydic = {')':'(' , 
        '}': '{' , ']': '['}
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top!=mydic[ch]:
                    return False
        return len(stack) == 0