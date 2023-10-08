# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rs = []
        def dfs(root):
            if root != None:
                dfs(root.left)
                rs.append(root.val)
                dfs(root.right)
 
        dfs(root)
        return rs