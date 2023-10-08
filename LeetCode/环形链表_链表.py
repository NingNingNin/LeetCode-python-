# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        
        sin = head.next
        dou = head.next.next


        while sin!=None and dou!=None:
            if(sin == dou) : return True
            sin = sin.next
            if dou.next is None:
                return False
            dou = dou.next.next

        return False

