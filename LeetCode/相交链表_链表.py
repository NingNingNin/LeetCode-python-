# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        lengthA,lengthB = 0,0
        curA,curB = headA,headB
        while(curA!=None): #求链表A的长度
            curA = curA.next
            lengthA +=1
        
        while(curB!=None): #求链表B的长度
            curB = curB.next
            lengthB +=1
        
        curA, curB = headA, headB

        if lengthB>lengthA: #让curA为最长链表的头，lenA为其长度
            lengthA, lengthB = lengthB, lengthA
            curA, curB = curB, curA

        gap = lengthA - lengthB #求长度差
        while(gap!=0): 
            curA = curA.next #让curA和curB在同一起点上
            gap -= 1
        
        while(curA!=None):
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
