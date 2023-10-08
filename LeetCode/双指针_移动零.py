class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i,j = 0,0
        len1 = len(nums)-1
        while j < len1 and nums[j] != 0 :
            j = j + 1

        i = j


        while j < len1 :
            j = j + 1
            if nums[j] != 0 :
                a = nums[j]
                nums[j] = nums[i]
                nums[i] = a
                i = i + 1

        return nums
 

