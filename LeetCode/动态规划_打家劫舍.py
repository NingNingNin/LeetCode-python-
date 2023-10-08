class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)== 1 :
            return nums[0]
        
        if len(nums)== 2 :
            return max(nums[0],nums[1])
        

        array = [0]* len(nums)
        array[0] = nums[0]
        array[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            array[i]= max(array[i-1],array[i-2]+nums[i])

        return array[len(nums)-1]