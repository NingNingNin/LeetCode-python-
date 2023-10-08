# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self) :
        self.MAX = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


        def depth(root) :
            if root ==None :return 0
            
            a = depth(root.left)
            b = depth(root.right)
            
            if a+b > self.MAX : self.MAX = a+b

            
            
            return max(a,b)+1
        
        depth(root)
        return self.MAX