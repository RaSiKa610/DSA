class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(i, current_combo, current_sum):
            if current_sum == target:
                res.append(list(current_combo))
                return

            if current_sum > target or i >= len(candidates):
                return

            current_combo.append(candidates[i])
            backtrack(i, current_combo, current_sum + candidates[i])

            current_combo.pop()

            backtrack(i+1, current_combo, current_sum)

        backtrack(0, [], 0)
        return res
