class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans = []
        sample = "123456789"
        low_len = len(str(low))
        high_len = len(str(high))
        for length in range(low_len, high_len+1):
            for start in range(10 - length):
                num = int(sample[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans
