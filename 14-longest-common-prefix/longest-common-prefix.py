class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0]

        for i , ch in enumerate(first):
            for s in strs[1:]:
                if i == len(s) or ch != s[i]:
                    return first[:i]
        return first