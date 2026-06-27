class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        n = len(manager)
        self.children =[[] for _ in range(n)]

        for emp in range(0, n):
            if emp != headID:
                self.children[manager[emp]].append(emp)

        def dfs(node):
            if not self.children[node]:
                return 0

            max_time = 0

            for emp in self.children[node]:
                path = dfs(emp)
                
                max_time = max(max_time, path)

            return informTime[node] + max_time

        return dfs(headID)
