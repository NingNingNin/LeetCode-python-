class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)

        stack = []
        stack.append(-1)
        maxlen = 0

        for i in range(length):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                stack.pop()
                if stack :
                    maxlen = max(maxlen, i - stack[-1])
                    
                if not stack:
                   stack.append(i)

        return maxlen
