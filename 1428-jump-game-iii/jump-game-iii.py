class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        queue = deque([start])
        seen = {start}

        while queue:
            i = queue.popleft()
            if(arr[i] == 0):
                return True

            for new in (arr[i] + i, i - arr[i]):
                if  0 <= new < len(arr) and new not in seen:
                    seen.add(new)
                    queue.append(new)
                       
        return False