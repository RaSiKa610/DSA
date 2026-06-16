class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
    
        result = [[1]]
        for i in range(1, numRows):
            prev = result[-1]
            new = [1]
            for j in range(len(prev) - 1):
                new.append(prev[j] + prev[j+1])
            new.append(1)
            result.append(new)
            

        return result
        