# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = []

        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                res.append(int("".join(path)))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.pop()

        dfs(root, [])
        return sum(res)            
