class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        current_capacity = capacity
        steps = 0
        for i in range(len(plants)):
            steps += 1
            current_capacity -= plants[i]
            if i + 1 < len(plants) and current_capacity < plants[i+1]:
                current_capacity = capacity
                steps += 2 * (i + 1)
        return steps
