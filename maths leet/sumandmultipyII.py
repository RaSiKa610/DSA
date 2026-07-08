class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        
        v = []
        for i, ch in enumerate(s):
            if ch != '0':
                v.append((i, int(ch)))

        n = len(v)
        if n == 0:
            return [0] * len(queries)

        pref_sum = [0] * (n+1)
        pref_val = [0] * (n+1)
        pow10 = [1] * (n+1)

        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + v[i][1]
            pref_val[i+1] = (pref_val[i] * 10 + v[i][1]) % MOD
            pow10[i+1] = (pow10[i] * 10) % MOD

        next_nz = [n] * len(s)
        prev_nz = [-1]  * len(s)
        idx = 0
        for i in range(len(s)):
            while idx < n and v[idx][0] < i:
                idx += 1 
            next_nz[i] = idx

        idx = n - 1
        for i in range(len(s) - 1, -1, -1):
            while idx >= 0 and v[idx][0] > i:
                idx -= 1
            prev_nz[i] = idx

        res = []
        for l, r in queries:
            v_l = next_nz[l]
            v_r = prev_nz[r]

            if v_l> v_r:
                res.append(0)
            else:
                sum_x = pref_sum[v_r + 1] - pref_sum[v_l] 
                length = v_r - v_l + 1
                ans = (pref_val[v_r + 1] - pref_val[v_l] * pow10[length]) % MOD

                res.append((sum_x * ans) % MOD)

        return res
