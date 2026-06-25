# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(node, r, curr_path):
            if not node:
                return

            curr_path.append(node.val)

            if not node.left and not node.right:
                if r == node.val:
                    res.append(list(curr_path))
            else:
                dfs(node.left, r - node.val, curr_path)
                dfs(node.right, r - node.val, curr_path)

            curr_path.pop()

        dfs(root, targetSum, [])
        return res
