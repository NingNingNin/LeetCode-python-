# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.count =0
        self.result =-1
        

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
    
        if root ==None :return
        if self.result != -1 :return
        self.kthSmallest(root.left,k)

        self.count += 1
        if self.count ==k :
            self.result = root.val
        self.kthSmallest(root.right,k)

        if self.result != -1 : return self.result

