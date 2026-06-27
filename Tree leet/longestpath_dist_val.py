class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        n = len(parent)
        self.children = [[] for _ in range(n)]
        for i in range(1, n):
            self.children[parent[i]].append(i)

        self.count = 0

        def dfs(node):
            max1 = 0
            max2 = 0


            for i in self.children[node]:
                child_path = dfs(i)

                if s[node] != s[i]:
                    if child_path > max1:
                        max2 = max1
                        max1 = child_path   
                    elif child_path > max2:
                        max2 = child_path
                                   
            self.count = max(self.count, max1 + max2 + 1)

            return max1 + 1

        dfs(0)
        return self.count
