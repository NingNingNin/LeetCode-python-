class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """


        hang = len(board)
        lie = len(board[0])
        lenword = len(word)
        flag = False
       

        def find(epoch,i,j,isvisit):
            if epoch>lenword-1 :
                return False
            if board[i][j] == word[epoch] :
                if epoch==lenword-1:
                   return True
                else:
                    isvisit[i][j] = 1
                    for k, l in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= k < hang and 0 <= l < lie and isvisit[k][l] == 0:
                            if find(epoch + 1, k, l, isvisit):
                                return True
                    isvisit[i][j] = 0
                        

        

        for dd in range(hang):
            for uu in range(lie):
                isvisit = [[0] * lie for _ in range(hang)]
                if find(0,dd,uu,isvisit):
                    flag = True

        return flag

                 