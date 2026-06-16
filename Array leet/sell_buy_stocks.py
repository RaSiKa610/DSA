class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_pro = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_pro:
                max_pro = i - min_price

        return max_pro