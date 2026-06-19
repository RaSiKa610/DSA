class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()

        if not s:
            return 0
        
        sign = 1
        i = 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        r = 0
    
        while i < len(s) and s[i].isdigit():
            r = r * 10 + int(s[i])
            i += 1

        r *= sign

        mini = -2**31
        maxi = 2**31 -1

        if r < mini:
            return mini
        if r > maxi:
            return maxi
        
        return r
