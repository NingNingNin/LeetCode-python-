from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = []
        array_list = deque()
        array_list.append(root)
        array_list.append('&')
        list1 = []

        while(array_list):
            q = array_list.popleft()
            if q == None : continue
            if q == '&' and not array_list  : return result
            if q == '&':  
                result.append(list1)
                list1 = []
                array_list.append('&')


            elif q !=None : 
                array_list.append(q.left) 
                array_list.append(q.right)
                list1.append(q.val)
        
        
       

            

