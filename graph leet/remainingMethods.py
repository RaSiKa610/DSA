from collections import deque

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]
        sus = [False] * n

        for u,v in invocations:
            adj[u].append(v)

        que = deque([k])
        sus[k] = True

        while que:
            curr = que.popleft()
            for neigh in adj[curr]:
                if not sus[neigh]:
                    sus[neigh] = True
                    que.append(neigh)
                    
        for u, v in invocations:
            if not sus[u] and sus[v]:
                return(list(range(n)))

        result = []
        for i in range(n):
            if not sus[i]:
                result.append(i)


        return result
                
