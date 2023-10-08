class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums)-1
            while j<k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append((nums[i],nums[j],nums[k]))
                    while j<len(nums)-1 and nums[j] == nums[j+1]:
                        j += 1
                    while k>0 and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else :
                    j += 1
 
        return result
            