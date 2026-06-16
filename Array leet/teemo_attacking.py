class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        r = 0
        
        for i in range(len(timeSeries) - 1):
            diff = timeSeries[i+1] - timeSeries[i]
            if diff < duration:
                r += diff
            else:
                r += duration
        return r + duration