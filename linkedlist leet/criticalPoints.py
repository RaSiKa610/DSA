# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head.next.next:
            return [-1,-1]
        prev = head
        curr = prev.next
        nxt = curr.next
        count = 1
        arr = []

        while nxt:
            if (prev.val < curr.val > nxt.val) or (prev.val > curr.val < nxt.val):
                arr.append(count)

            prev = curr
            curr = nxt
            nxt = nxt.next
            count += 1

        if len(arr) < 2:
            return [-1,-1]

        max_dist = arr[-1] - arr[0]
        min_dist = float('inf')
        for i in range(1, len(arr)):
            min_dist = min(min_dist, arr[i] - arr[i-1])

        return [min_dist, max_dist]
