class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        def check(diff):
            count = 1
            last = price[0]
            for i in range(1, len(price)):
                if price[i] - last >= diff:
                    count += 1
                    last = price[i]

            return count >= k

        l = 0
        r = price[-1] - price[0]
        ans = 0

        while l <= r:
            mid =(l + r) // 2
            if check(mid):
                ans = mid
                l = mid +1
            else:
                r = mid - 1
        return ans
