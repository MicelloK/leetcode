class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse_substring(s, start, end):
            return s[:start+1] + s[start+1:end][::-1] + s[end:]

        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    start = stack.pop()
                    s = reverse_substring(s, start, i)

        return s.replace('(', '').replace(')', '')