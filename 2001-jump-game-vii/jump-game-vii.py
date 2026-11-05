class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        if(s[0] != '0'):
            return False
        
        queue = deque([0])

        farthest = 0

        while queue:
            i = queue.popleft()

            start = max(farthest + 1, i + minJump)   
            end = min(i + maxJump, len(s) - 1)

            for j in range(start , end + 1):
                if(s[j] == '0'):
                    if(j == len(s) - 1):
                        return True
                    queue.append(j)

                farthest = max(farthest, end)
            
        return False