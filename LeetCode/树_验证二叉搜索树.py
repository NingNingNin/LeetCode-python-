# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def judge(root,minz,maxz):
            if root ==None : return True
            if root.left != None :
                 if root.val <= root.left.val:
                     return False
                 
            if root.right != None :
                 if root.val >= root.right.val:
                     return False
            
            if root.val <=minz or root.val >=maxz :
                return False
                 
            return judge(root.left,minz,root.val) and judge(root.right,root.val,maxz)
        
        return judge(root,float('-inf'),float('inf'))
            