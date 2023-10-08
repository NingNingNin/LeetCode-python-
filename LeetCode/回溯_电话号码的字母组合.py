class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == "":
            return []
        
        hashmap = { "2": "abc",
             "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",}
        

        length = len(digits)

        res = []
        str = ""

        def product(epoch,str):
           if epoch== length:
               res.append(str)
               return
           else: 
               strin = hashmap[digits[epoch]]
               for i in range(len(strin)):
                   str = str + strin[i]
                   product(epoch+1,str)
                   str = str[:-1]
                 
               

        product(0,str)
        return res

