class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        for i in s:
            if(i != '#'):
                stack1.append(i)
            elif(stack1):
                stack1.pop() 
            else:
                continue

        for x in t:
            if(x != '#'):
                stack2.append(x)
            elif(stack2):
                stack2.pop()
            else:
                continue

        return stack1 == stack2