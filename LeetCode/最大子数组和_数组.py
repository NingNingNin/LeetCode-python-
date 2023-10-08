class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_array = [0] * len(nums)
        my_array[0] = nums[0]
 
        for i in range(1,len(nums)):
            if(nums[i] + my_array[i-1] > nums[i]):  my_array[i] = nums[i] + my_array[i-1]
            else: my_array[i] = nums[i]
  
        max1 = max(my_array)
        print(my_array)
        return max1
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
Sol = Solution()
result = Sol.maxSubArray(nums)

print(result)