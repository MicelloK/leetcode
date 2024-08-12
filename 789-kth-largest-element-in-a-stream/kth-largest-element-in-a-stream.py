class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.nums) and self.nums[i] > val:
            i += 1
        self.nums = self.nums[:i] + [val] + self.nums[i:]
        if len(self.nums) < self.k:
            return None
        return self.nums[self.k-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)