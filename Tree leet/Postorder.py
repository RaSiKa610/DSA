# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        self.li = []

        def helper(node):
            if not node:
                return

            helper(node.left)
            helper(node.right)
            self.li.append(node.val)

        helper(root)
        return self.li
