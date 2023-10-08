# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head_node = ListNode(1)
        head = head_node
        sum = 0
        while l1 != None or l2 != None or sum :
            if l1 != None: 
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            head_node.next = ListNode(sum%10)
            sum = sum//10
            head_node = head_node.next
        
        return head.next


        