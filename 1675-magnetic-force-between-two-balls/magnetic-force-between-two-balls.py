class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = position[len(position)-1]

        max_force = 0
        while l <= r:
            mid = l + (r - l) // 2
            # check
            placed = 1
            last_pos = position[0]
            for pos in position:
                if pos - last_pos >= mid:
                    placed += 1
                    last_pos = pos
                if placed >= m:
                    max_force = mid
                    break
                
            if placed >= m:
                l = mid + 1
            else:
                r = mid - 1

        return max_force
            

