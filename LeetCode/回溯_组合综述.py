class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        length = len(candidates)
        res = []

        def bfs(num=0,result=[],start=0):
           for i in range(start,length):
               if num == target: 
                  res.append(result[:])
                  return
               if num + candidates[i] <=target:
                   result.append(candidates[i])
                   bfs(num + candidates[i],result,i)
                   result.pop(-1)


        bfs()
        return res