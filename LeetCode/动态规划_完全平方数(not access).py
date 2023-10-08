import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n ==1 :return 1



        row = 0
        while row**2 < n:
            row += 1


        f = [[sys.maxsize]*(n+1) for _ in range(row)]
        f[0][0] = 0

        for i in range(1,row):
            for j in range(n+1):
                if(i*2>j): 
                    f[i][j] = f[i-1][j]
                else:
                    f[i][j] = min(f[i-1][j],f[i][j-i**2]+1)

        return f[row-1][n] 