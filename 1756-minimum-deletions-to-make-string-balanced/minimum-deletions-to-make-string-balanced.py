class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = s.count('a')
        b_count = 0

        result = len(s)
        for ch in s:
            if ch == 'a':
                a_count -= 1
            result = min(result, a_count + b_count)
            if ch == 'b':
                b_count += 1
        return result
            
            
            
