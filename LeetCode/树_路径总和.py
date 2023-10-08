# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self) :
        self.count =0

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if root is None: return self.count
         
        def sum1(root,num):
            if root != None:
                num  = num + root.val
                if num == targetSum:
                    self.count = self.count +1
                sum1(root.left,num)
                sum1(root.right,num)

        def traverse(root):
            if root != None:
                sum1(root,0)
                traverse(root.left)
                traverse(root.right)
            
        traverse(root)
        return self.count


        

        