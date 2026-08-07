class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def get_min_length(target):
            """Calculates the minimum number of single digits needed to multiply to `target`."""
            count = 0
            temp = target
            for d in range(9, 1, -1):
                while temp % d == 0:
                    count += 1
                    temp //= d
            return count if temp == 1 else float('inf')

        def slotfiller(required_num, length):
            s = []
            temp = required_num
            for i in range(9, 1, -1):
                while temp % i == 0:
                    s.append(str(i))
                    temp //= i
            
            if temp > 1 or len(s) > length:
                return None
            
            s.extend(['1'] * (length - len(s)))
            s.sort()
            return "".join(s)

        n = len(num)
        
        # Step 1: Verify t only contains prime factors 2, 3, 5, 7
        temp_t = t
        for p in (2, 3, 5, 7):
            while temp_t % p == 0:
                temp_t //= p
        if temp_t > 1:
            return "-1"

        # Step 2: Precompute remaining factors needed
        remainingFactor = [t] * (n + 1)
        for i in range(n):
            curr = int(num[i])
            if curr == 0:
                break
            remainingFactor[i + 1] = remainingFactor[i] // gcd(remainingFactor[i], curr)

        # Step 3: Check if num itself works
        if '0' not in num and remainingFactor[n] == 1:
            return num

        # Step 4: Backtrack to find same-length prefix match
        firstZero = num.find('0')
        limit = firstZero if firstZero != -1 else n - 1

        for i in range(limit, -1, -1):
            required = remainingFactor[i]
            freeSlots = n - 1 - i
            
            startDigit = max(1, int(num[i]) + 1)
            for digit in range(startDigit, 10):
                further_required = required // gcd(required, digit)
                requiredNumber = slotfiller(further_required, freeSlots)

                if requiredNumber is not None:
                    return num[:i] + str(digit) + requiredNumber

        # Step 5: Construct shortest valid number longer than `n`
        min_len = get_min_length(t)
        target_len = max(n + 1, min_len)
        return slotfiller(t, target_len)
