# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None : return True
        
        
        root1 = root.left
        root2 = root.right
        def  isSymmet(root1,root2):
            if root1 == None and root2 ==None:
                return True
            if root1 == None or root2 ==None:
                return False
            if root2.val != root1.val : return False
            else:
                return isSymmet(root1.left,root2.right) and isSymmet(root1.right,root2.left)
            
        return isSymmet(root1,root2)

        