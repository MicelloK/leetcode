class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median(nums: List[int]) -> float:
            if len(nums) % 2 == 1:
                return nums[len(nums)//2]
            else:
                return (nums[len(nums)//2] + nums[len(nums)//2-1]) / 2

        if not nums1:
            return median(nums2)
        if not nums2:
            return median(nums1)

        while True:
            if len(nums2) < len(nums1):
                nums1, nums2 = nums2, nums1

            if nums1[len(nums1)-1] <= nums2[0]:
                return median(nums1 + nums2)
            if nums2[len(nums2)-1] <= nums1[0]:
                return median(nums2 + nums1)

            if len(nums1) <= 2 or len(nums2) <= 2:
                return median(sorted(nums1+nums2)) # tu trzeba binarysearcha zrobić, ale mi się nie chciało

            m1 = median(nums1)
            m2 = median(nums2)

            if m1 == m2:
                return m1
            elif m1 > m2:
                nums2 = nums2[(len(nums1)-1)//2:]
                nums1 = nums1[:-((len(nums1)-1)//2)]
            else:
                nums2 = nums2[:-((len(nums1)-1)//2)]
                nums1 = nums1[(len(nums1)-1)//2:]
