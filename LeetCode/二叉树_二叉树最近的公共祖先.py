# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def __init__(self) :
        self.ans = TreeNode(0)
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """


        def  postorder(root,p,q):
            if root == None:
                return False
           
          
            left =  postorder(root.left,p,q)
            right = postorder(root.right,p,q)

            if(left and right) : 
                self.ans = root
                return False
            
            if (root==p or root==q):
                if (left or right):
                    self.ans=root
                
                return True
            
            
            if(left or right) : return True

        postorder(root,p,q)
        return self.ans
           






        