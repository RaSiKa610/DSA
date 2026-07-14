# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        p = head
        length = 0
        while p:
            length += 1
            p = p.next

        first = head
        for _ in range(k-1):
            first = first.next

        last = head
        for _ in range(length - k):
            last = last.next

        first.val, last.val = last.val, first.val

        return head
