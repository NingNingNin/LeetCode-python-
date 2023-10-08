class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i,j = 0,len(nums)-1

        while i<=j:
            middle = (i+j)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] >= nums[i]:
                if target <= nums[middle] and target >= nums[i]:
                    j = middle - 1
                else: i = middle + 1
            elif nums[middle] <= nums[i]:
                if target >= nums[middle] and target <= nums[j]:
                    i = middle +1
                else: j = middle - 1

        return -1

            



