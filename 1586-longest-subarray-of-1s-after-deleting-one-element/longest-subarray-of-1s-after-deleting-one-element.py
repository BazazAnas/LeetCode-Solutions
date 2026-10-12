class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        size = 0
        zeroes = 0
        while r < len(nums):
                
            if(nums[r] == 0):
                zeroes += 1
            

            while zeroes > 1:
                if(nums[l] == 0):
                    zeroes -= 1
                l += 1

            size = max(size, r - l)
            r += 1
        return size