class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = {}

        for object in strs:
            sequence = ''.join(sorted(object))
            if sequence in hash_map:
                hash_map[sequence].append(object)
            else: hash_map[sequence] = [object]
        
        list1 = list(hash_map.values())
        return list1
      
    