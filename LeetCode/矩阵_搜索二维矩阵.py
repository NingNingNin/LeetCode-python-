class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = len(matrix)
        column = len(matrix[0])
        
        i,j = 0 , column-1

        while 0<=i<row and 0<=j<column:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j]< target:
                i += 1
            else :
                j -= 1
        
        return False




        