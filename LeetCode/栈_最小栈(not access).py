class MinStack(object):

    def __init__(self):
        self.min = int('inf')
        self.stack1 = []



    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack1.append(val)
        if val < self.min:
           self.min = val 


    def pop(self):
        """
        :rtype: None
        """
        x = self.stack1[-1]
        self.stack1.pop()
        if self.stack1!=[] and x ==self.min:
            self.min = min(self.stack1)

        return x
        


    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()