class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        p = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    p += 4
                    if r > 0 and grid[r-1][c] == 1:
                        p -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        p -= 2

        return p