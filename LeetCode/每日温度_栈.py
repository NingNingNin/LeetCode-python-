from collections import deque


class Solution(object):

    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = deque()
        stack.append((0,temperatures[0]))
        result = [0]*len(temperatures)

        for i in range(1,len(temperatures)):
            top = stack[-1]
            while(stack and temperatures[i] >top[1]):
                result[top[0]] = i - top[0]
                stack.pop()
                if stack : 
                    top = stack[-1]
            stack.append((i,temperatures[i]))
            
        
        while(stack):
            top = stack.pop()
            result[top[0]] = 0

        return result

