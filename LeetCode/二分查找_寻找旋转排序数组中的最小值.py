class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        i,j = 0,len(nums)-1
        min1 = 10000
        while i<=j and i<=len(nums)-1 and j >=0:
            middle = (i+j)//2
            min1 = min(min1,nums[i])
            min1 = min(min1,nums[middle])
            min1 = min(min1,nums[j])
            if nums[middle] >= nums[i]:
                    i = middle +1
                
            else: 
                    j = middle - 1

        return min1