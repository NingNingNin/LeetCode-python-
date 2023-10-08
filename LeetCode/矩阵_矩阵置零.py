class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """


        list = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    list.append((i,j))

        
        while list :
            i,j = list[-1]
            for y in range(len(matrix)):
                  matrix[y][j] = 0
            for y in range(len(matrix[0])):
                  matrix[i][y] = 0

            list.pop()
