class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindroms_dict = {}

        def palindroms(start: int) -> List[List[str]]:
            result = []
            for i in range(start, len(s)):
                sub = s[start:i+1]
                if sub == sub[::-1]:
                    if i == len(s) - 1:
                        result.append([sub])
                    else:
                        if i+1 not in palindroms_dict:
                            palindroms_dict[i+1] = palindroms(i+1)
                        for pal in palindroms_dict[i+1]:
                            result.append([sub] + pal)
            return result

        return palindroms(0)

                        
