from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        
        length = len(s)
        i = 0
        while i<length :
            if(s[i] == '(' or s[i] == '[' or s[i] == '{' ): stack.append(s[i])
            elif(s[i]== ')'):
                if not stack or stack[-1] != '(':return False 
                else: stack.pop()
            elif(s[i]== ']'):
                if not stack or stack[-1] != '[':return False 
                else: stack.pop()
            elif(s[i]== '}'):
                if not stack or stack[-1] != '{':return False 
                else: stack.pop()
            i = i + 1

        if len(stack) == 0 : return True
        else : return False
