class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        current_flips = 0
        queue = deque()
        
        for i in range(n):
            if queue and queue[0] == i:
                queue.popleft()
                current_flips -= 1
            
            if (nums[i] + current_flips) % 2 == 0:
                if i + k > n:
                    return -1
                flip_count += 1
                current_flips += 1
                queue.append(i + k)
        
        return flip_count