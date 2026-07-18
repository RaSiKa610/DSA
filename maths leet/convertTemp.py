class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """

        ans = [(celsius + 273.15), ((celsius * 1.80)+ 32.00)]
        return ans
