class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()

        count_elements = {num: nums.count(num) for num in nums}
        rejected_elements = {num: False for num in nums}
        def beautiful_subsets_num(i: int) -> int:
            if i >= len(nums):
                return 0
            if i + count_elements[nums[i]] >= len(nums):
                if rejected_elements[nums[i]]:
                    return 1
                else:
                    return 2 ** count_elements[nums[i]]

            result = beautiful_subsets_num(i+count_elements[nums[i]])
            if not rejected_elements[nums[i]]:
                rejected_elements[nums[i]+k] = True
                result += (2 ** count_elements[nums[i]] - 1) * beautiful_subsets_num(i+count_elements[nums[i]])
                rejected_elements[nums[i]+k] = False
            return result
        
        return beautiful_subsets_num(0) - 1
                

            




            

        

        
