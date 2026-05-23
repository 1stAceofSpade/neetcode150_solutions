class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        size = len(tokens)
        for tok in tokens:
            if tok == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif tok == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif tok == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif tok == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(tok))
        return stack[-1]