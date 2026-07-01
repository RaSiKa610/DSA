# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []

        for i,l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
