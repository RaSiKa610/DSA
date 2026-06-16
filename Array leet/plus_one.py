class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = str(int("".join(str(x) for x in digits)) + 1)
        answer = [int(x) for x in result]
        return answer