class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        i,j = 0,0
        array = [0] * 260
        max_length = 0

        while j <= len(s) -1 :
           num = ord(s[j])
           if array[num] == 0 :
               array[num] = 1 
           
           elif array[num] == 1 :
               while(s[i] != s[j]):
                   array[ord(s[i])] = 0
                   i += 1
               i += 1
            

           if j-i+1 > max_length : max_length = j-i+1
           j += 1 

        return max_length