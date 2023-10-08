import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        f = [[sys.maxsize]* (amount+1) for _ in range(len(coins)+1)]

        f[0][0] = 0


        for i in range(1,len(coins)+1):
            for j in range(0,amount+1):
                  if coins[i-1]> j :
                        f[i][j] = f[i-1][j]
                  else:
                        f[i][j] = min(f[i-1][j],f[i][j-coins[i-1]]+1)


        return f[len(coins)][amount] if f[len(coins)][amount] < 1000000 else -1



