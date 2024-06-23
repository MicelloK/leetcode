class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        j = 0
        max_len = 1
        min_num = nums[0]
        max_num = nums[0]
        elements = {nums[0]: 0}
        
        while j < len(nums) - 1:
            j += 1
            elements[nums[j]] = j
            if nums[j] > max_num:
                max_num = nums[j]
                while max_num - min_num > limit:
                    while elements and elements[min(elements)] < i:
                        elements.pop(min(elements))
                    if elements:
                        i = min(elements.pop(min(elements)) + 1, j)
                    else:
                        i = j
                    while elements and elements[min(elements)] < i:
                        elements.pop(min(elements))
                    if elements:
                        min_num = min(elements)
                    else:
                        min_num = nums[i]

            elif nums[j] < min_num:
                min_num = nums[j]
                while max_num - min_num > limit:
                    while elements and elements[max(elements)] < i:
                        elemetns.pop(max(elements))
                    if elements:
                        i = min(elements.pop(max(elements)) + 1, j)
                    else:
                        i = j
                    while elements and elements[max(elements)] < i:
                        elements.pop(max(elements))
                    if elements:
                        max_num = max(elements)
                    else:
                        max_num = i

            max_len = max(max_len, j - i + 1)
            
        return max_len

