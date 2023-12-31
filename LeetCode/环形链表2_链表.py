# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None : return None

        if head.next == None : return None
        
        slow = head.next 
        fast = slow.next

        if fast == None :return None

        while fast!= None and fast.next != None and slow != fast:
            slow = slow.next
            fast = fast.next.next

        if slow != fast : return None
        
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow