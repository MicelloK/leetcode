class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        result = 0
        first = 'ab'
        second = 'ba'

        if y > x:
            first, second = second, first
            x, y = y, x

        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 2 and ''.join(stack[-2:]) == first:
                result += x
                stack.pop()
                stack.pop()

        s = ''.join(stack)
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 2 and ''.join(stack[-2:]) == second:
                result += y
                stack.pop()
                stack.pop()
        
        return result