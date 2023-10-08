class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i,j = 0,len(nums)-1
        result = 0

        while i <= j:
            middle = (i+j)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target :
                j = middle - 1
            else:
                i = middle + 1
            result = i
        
        return result

        