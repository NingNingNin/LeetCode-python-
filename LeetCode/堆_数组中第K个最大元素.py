import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,nums[i])
        


        lar = heapq.nlargest(k,heap)
        result = lar[-1]

        return result