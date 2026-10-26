class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:                  
                return 0

            total = grid[r][c]                  
            grid[r][c] = 0                      
            total += dfs(r + 1, c)
            total += dfs(r - 1, c)
            total += dfs(r, c + 1)
            total += dfs(r, c - 1)
            return total

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:              
                    if dfs(r, c) % k == 0:
                        count += 1
        return count