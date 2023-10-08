class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_array = [0] * (len(nums)+1)

        for i in range(0,len(nums)):
            if(nums[i]>0 and nums[i]<len(my_array)):
              my_array[nums[i]] +=1
        
        for i in range(1,len(my_array)):
            if(my_array[i] ==0):
                return i

        return len(nums)+1

      
            

nums = [2]
Sol = Solution()
result = Sol.firstMissingPositive(nums)
print(result)