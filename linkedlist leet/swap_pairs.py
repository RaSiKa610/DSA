# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p = ListNode(0)
        p.next = head

        prev = p

        while prev.next and prev.next.next:
            i = prev.next
            j = prev.next.next

            i.next = j.next
            j.next = i
            prev.next = j

            prev = i

        return p.next
