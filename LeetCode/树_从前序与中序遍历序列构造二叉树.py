# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(preorder, h, i, inorder, j, k):
            if h > i or j > k:
                return None
            
            root_val = preorder[h]
            root = TreeNode(root_val)
            pivot = inorder.index(root_val)

            root.left = build(preorder, h+1, pivot+h-j, inorder, j, pivot-1)
            root.right = build(preorder, h+pivot+1-j, i, inorder, pivot+1, k)

            return root

        return build(preorder, 0, len(preorder)-1, inorder, 0, len(preorder)-1)
