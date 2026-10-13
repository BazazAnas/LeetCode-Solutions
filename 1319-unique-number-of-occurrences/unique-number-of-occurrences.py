class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = {}
        for n in arr:
            count[n] = count.get(n, 0) + 1
        
        if len(set(count.values())) == len(count.values()):
            return True
        else:
            return False
        
        