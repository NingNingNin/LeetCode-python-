class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(nums)
        count = 0
        max1 =  0
        for ob in nums:
            t = ob
            if ob-1 not in hashset:
                 count = 1
                 
                 while t + 1 in hashset:
                     count = count +1
                     t = t + 1     
        
            max1 = max(max1,count)
            count = 0

        return max1