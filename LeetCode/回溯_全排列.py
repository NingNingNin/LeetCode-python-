class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        def backTrack(first=0):
           if n == first :
               res.append(nums[:])
           for i in range(first,n):
               nums[first] , nums[i] = nums[i] , nums[first]
               backTrack(first+1)
               nums[first] , nums[i] = nums[i] , nums[first]

        
        backTrack()
        return res
                

