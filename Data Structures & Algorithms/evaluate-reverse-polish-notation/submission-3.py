class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stack.append(tokens[0])
        operators = {'+', '-', '*', '/'}
        for i in range(1, len(tokens)):
            if tokens[i] in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(str(int(eval(a + tokens[i] + b))))
            else:
                stack.append(tokens[i])
        return int(stack.pop())