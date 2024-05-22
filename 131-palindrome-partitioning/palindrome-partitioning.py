class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindroms(start: int) -> List[List[str]]:
            result = []
            for i in range(start, len(s)):
                sub = s[start:i+1]
                if sub == sub[::-1]:
                    if i == len(s) - 1:
                        result.append([sub])
                    else:
                        next_palindroms = palindroms(i+1)
                        for pal in next_palindroms:
                            result.append([sub] + pal)
            return result

        return palindroms(0)

                        
