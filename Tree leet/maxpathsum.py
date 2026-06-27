# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')

        def gain(node):
            if not node:
                return 0

            l = max(gain(node.left), 0)
            r = max(gain(node.right), 0)

            curr_arch = node.val + l + r

            self.max_sum = max(self.max_sum, curr_arch)

            return node.val + max(l, r)

        gain(root)
        return self.max_sum
