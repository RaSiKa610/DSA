class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            r = a % b
            while r!=0:
                a = b
                b = r
                r = a % b

            return b
        
        n = len(nums)
        prefixGcd = []
        mx = 0
        for i in range(n):
            mx = max(nums[i], mx)
            prefixGcd.append(gcd(mx, nums[i]))

        prefixGcd.sort()
        l = 0
        r = n - 1
        s = 0 
        while l < r:
            s += gcd(prefixGcd[r],prefixGcd[l])
            l += 1
            r -= 1

        return s
