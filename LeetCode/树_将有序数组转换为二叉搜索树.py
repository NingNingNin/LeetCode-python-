# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def sorte(num,a,b):
            if a>b:
                return 
            mid = (a+b)/2
            tree = TreeNode(None)
            tree.val = num[mid]
            
            tree.left = sorte(num,a,mid-1)
            tree.right = sorte(num,mid+1,b)
            
            return tree
    

        return sorte(nums,0,len(nums)-1)




