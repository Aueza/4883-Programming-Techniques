from collections import deque

# breadth first search algorithm
def bfs(startRow, startCol, grid):
    # Initialize a queue for BFS and add the starting cell
    queue = deque([(startRow, startCol)])
    # Define the four possible directions (up, down, left, right) for grid traversal
    directions = [(0,1), (0,-1), (-1,0),(1,0)]
    # While the queue is not empty
    while queue:
        # Pop the front element from the queue
        r, c = queue.popleft()
        # For each direction, compute the next cell's row and column
        for dr, dc in directions:
            newRow, newCol = r + dr, c + dc
        # Check if the next cell is within the grid bounds and is unvisited land
            if 0 <= newRow < len(grid) and 0<= newCol < len(grid[0]) and grid[newRow][newCol] == '1':
        # If valid, mark the cell as visited and add it to the queue
                grid[newRow][newCol] = '0'
                queue.append((newRow, newCol))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Initialize a counter to keep track of the number of islands
        islandCount = 0
        # Traverse the entire grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # When you find unvisited land
                if grid[row][col] == '1':
                    # Perform BFS to mark the entire island starting from this cell
                    bfs(row,col,grid)
                    # Increment the island counter
                    islandCount += 1
        # Return the total number of islands
        return islandCount