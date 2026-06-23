class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        r = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2) -1, -1 ,-1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1

                t = mul + r[p2]
                r[p2] = t % 10
                r[p1] += t // 10

        s = 0
        while s < len(r) and r[s] == 0:
            s += 1

        return "".join(map(str, r[s:]))
