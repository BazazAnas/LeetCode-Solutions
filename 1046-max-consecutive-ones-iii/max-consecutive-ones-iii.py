class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zeroes = 0
        length = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            length = max(length, right - left + 1)

        return length
