class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        min_damage = [[float('inf')] * n for _ in range(m)]

        min_damage[0][0] = grid[0][0]
        queue = deque([(0,0)])
        actions = [(0,1), (1,0), (0,-1), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            if r == m-1 and c == n-1:
                break
            for dr, dc in actions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    next_damage = min_damage[r][c] + grid[nr][nc]
                    
                    if next_damage < min_damage[nr][nc]:
                        min_damage[nr][nc] = next_damage

                        if grid[nr][nc] == 0:
                            queue.appendleft((nr,nc))
                        else:
                            queue.append((nr, nc))

        return health - min_damage[m-1][n-1] >= 1
