class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_map = {'}':'{', ']':'[', ')':'('}
        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            elif stack and (stack[-1] == par_map[i]):
                stack.pop()
            else:
                return False
        return not stack