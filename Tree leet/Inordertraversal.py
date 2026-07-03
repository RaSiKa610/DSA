# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
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
            self.li.append(node.val)
            helper(node.right)


        helper(root)
        return self.li
