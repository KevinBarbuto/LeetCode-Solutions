# Objective: Find the perimeter of the grid-based island.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set() # visited gridpoints

        # Depth-first search
        def dfs(i, j):
            # Ensure that grid position is in-bounds
            if i >= len(grid) or j >= len(grid[0]) or \
            i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            # Avoid redundant checks
            if (i, j) in visited:
                return 0
            visited.add((i, j))

            # Calculate perimeter
            perimeter = dfs(i, j+1)
            perimeter += dfs(i+1, j)
            perimeter += dfs(i, j-1)
            perimeter += dfs(i-1, j)
            return perimeter
        
        # Find a grid with land to begin the DFS search
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)
