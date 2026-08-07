class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {r: i for i, r in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for j, r in enumerate(list2):
            if r in index_map:
                index_sum = j + index_map[r]

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [r]
                elif index_sum == min_sum:
                    result.append(r)

        return result
