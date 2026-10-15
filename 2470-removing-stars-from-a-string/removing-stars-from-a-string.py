class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for ch in s:
            if(ch != '*'):
                stack.append(ch)
            elif(ch == '*'):
                stack.pop()

        return "".join(stack)