class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        jump = 0
        curReach = 0
        maxReach = 0

        for i in range(n -1):
            maxReach = max(maxReach,i + nums[i])
            if(i == curReach):
                jump += 1
                curReach = maxReach    
        return jump
            