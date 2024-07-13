class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions), key=lambda x: x[0])
        stack = deque()
        
        for pos, health, direction in robots:
            while stack and stack[-1][2] == 'R' and direction == 'L':
                last_pos, last_health, last_direction = stack.pop()
                if health > last_health:
                    health -= 1
                elif health < last_health:
                    last_health -= 1
                    stack.append((last_pos, last_health, last_direction))
                    break
                else:
                    break
            else:
                stack.append((pos, health, direction))
        
        result_dict = {pos: health for pos, health, direction in stack}
        return [result_dict.get(pos, 0) for pos in positions if result_dict.get(pos, 0) > 0]
