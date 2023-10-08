class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        i,j = 0,len(nums)-1
        k = -1

        while i <= j:
            middle = (i+j)//2
            if nums[middle] == target:
                k = middle
                break
            elif nums[middle] > target :
                j = middle - 1
            else:
                i = middle + 1

        if k == -1:
            return [-1,-1]
        
        else:
            i,j = k,k
            while 0<=i-1<len(nums) and nums[i-1] == nums[k]:
                i -= 1
            while 0<=j+1<len(nums) and nums[j+1] == nums[k]:
                j += 1
            return [i,j]
        
                



        
            
        

