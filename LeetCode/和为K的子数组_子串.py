class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        hash_map = {0:1}
        ss = 0

        for i in range(len(nums)):
            ss = ss + nums[i]
            if ss - k in hash_map:
               count = count +hash_map[ss - k]
            
            if ss in hash_map:
                hash_map[ss] += 1

            else : hash_map[ss] = 1

        return count

