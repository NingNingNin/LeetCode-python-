# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root ==None : return

        result =root
        while root:
            if root.left is not None:
                t = root.left
                ti = t
                while t.right is not None:
                    t = t.right
                
                t.right = root.right
                root.right = ti
                root.left = None


            root = root.right

        return result