# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nn = ListNode(0)
        nn.next =head
        index = head
        while n > 0 :
            index = index.next
            if index == None: return None
            n -= 1 
        
      

        index0 = head
        while index != None and index.next != None:
            index0 = index0.next
            index = index.next

            
        index0.next =index0.next.next

        return head
        
