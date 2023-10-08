from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        list = deque()
        list.append(0)
        for i in range(1,k):
            while list and nums[i] >= nums[list[-1]] : 
                list.pop()
            list.append(i)

        result = []
        max1 = nums[list[0]]
        result.append(max1)

        for i in range(k,len(nums)):
            if i - list[0] >= k : 
                list.popleft()
            while list and nums[i] >= nums[list[-1]] : 
                 list.pop()
            list.append(i)
            
            result.append(nums[list[0]])


        return result
                        


        