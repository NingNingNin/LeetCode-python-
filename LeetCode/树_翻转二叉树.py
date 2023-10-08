# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        head = root
        
        def invert(root):
            if root == None : return
            else :
                t = root.left
                root.left = root.right
                root.right =t
            invert(root.left)
            invert(root.right)
        
        invert(root)
        return head