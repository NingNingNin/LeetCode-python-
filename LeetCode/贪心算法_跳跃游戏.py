class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


        maxindex = 0
        if len(nums) ==1 : return True

        for i in range(len(nums)) :
            maxindex = max(maxindex,i+nums[i])
            if maxindex == i and nums[i] == 0 and i != len(nums)-1:
                return False
            
        return True
