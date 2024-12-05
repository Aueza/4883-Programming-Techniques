# This solution does work, but needs further optimization to pass the longest test case.

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        # init starting position
        x, y = 0, 0
        # using a set is more optimal (average O(1) lookup time)
        visited = set()
        visited.add((x, y))
        # up, left, down, right.
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)] 
        # start moving up.
        direction = 0 

        for dist in distance:
            dx, dy = directions[direction]

            # Move one step at a time to track positions
            for _ in range(dist):
                # moving in specific direction, one unit at a time for range(0, dist) times.
                x, y = x + dx, y + dy
                # path crosses itself.
                if (x, y) in visited:  
                    return True  
                visited.add((x, y))
            # Update direction after each move
            direction = (direction + 1) % 4
        # path does not cross.
        return False 
