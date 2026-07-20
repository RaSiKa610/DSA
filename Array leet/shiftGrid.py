class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        one_d = sum(grid, [])
        k %= len(one_d)
        one_d = one_d[-k:] + one_d[:-k]

        r, c = len(grid), len(grid[0])
        new_arr = [one_d[i*c:(i+1)*c] for i in range(r)]
        return new_arr
