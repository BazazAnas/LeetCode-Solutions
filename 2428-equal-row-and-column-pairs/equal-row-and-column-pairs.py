class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = {}
        count = 0

        for i in range(len(grid)):
            row = tuple(grid[i])
            seen[row] = seen.get(row,0) + 1
           
        for n in range(len(grid)):
            col = tuple([r[n] for r in grid])
            count += seen.get(col,0)

        return count   