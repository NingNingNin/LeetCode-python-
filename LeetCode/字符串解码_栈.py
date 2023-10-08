from collections import deque

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = deque()
        result = ''
        ss = ''
        chuan = ''
        i = 0
        while i < len(s):
            if(s[i] == '[') : 
                stack.append((chuan,int(ss)))
                chuan = ''
                ss = ''
                i = i + 1
            elif(s[i] >='a' and s[i] <= 'z'):
                chuan = chuan + s[i]
                i = i + 1
            elif(s[i]>='0' and s[i]<='9'):
                while(s[i]>='0' and s[i]<='9' and i < len(s)): 
                    ss = ss + s[i]
                    i = i + 1
            elif(s[i] == ']') : 
                a = stack.pop()
                chuan = a[0] + chuan * a[1]
                i = i + 1
                
            result = chuan

        return result