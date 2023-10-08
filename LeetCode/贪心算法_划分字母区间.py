class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        index = 0
        post = len(s)-1
        position = 0
        result = []
        before = 0
        
        while index <= len(s)-1:
            while s[post] != s[index]:
                post -= 1
            if post > position :
                position = post 
            if index == position :
                result.append(position-before+1)
                before = position+1
            index += 1
            post = len(s) -1


        return result
            
