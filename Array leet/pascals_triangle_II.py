class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        result = [[1]]
        for i in range(1, rowIndex + 1):
            prev = result[-1]
            new = [1]
            for j in range(len(prev) - 1):
                new.append(prev[j] + prev[j+1])
            new.append(1)
            result.append(new)

        return result[rowIndex]