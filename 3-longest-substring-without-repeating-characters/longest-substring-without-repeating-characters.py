class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest_substring_len = 1
        starting_pos = 0
        character_pos = {}

        for i in range(len(s)):
            if s[i] in character_pos and character_pos[s[i]] >= starting_pos:
                longest_substring_len = max(longest_substring_len, i - starting_pos)
                starting_pos = character_pos[s[i]] + 1
            
            character_pos[s[i]] = i

        longest_substring_len = max(longest_substring_len, len(s) - starting_pos)

            
            

        return longest_substring_len


