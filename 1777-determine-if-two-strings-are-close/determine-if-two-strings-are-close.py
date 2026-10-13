class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        word1d = {}
        word2d = {}
        for n in word1:
            word1d[n] = word1d.get(n,0) + 1
        for n in word2:
            word2d[n] = word2d.get(n,0) + 1

        

        if len(word1) == len(word2) and set(word1) == set(word2) and (
            sorted(word1d.values()) == sorted(word2d.values())
        ):
            return True
        else:
            return False 