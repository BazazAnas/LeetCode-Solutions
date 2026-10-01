class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')   # smallest value seen so far
        second = float('inf')  # smallest value that has something smaller before it

        for n in nums:
            if n <= first:
                first = n          # new smallest candidate
            elif n <= second:
                second = n         # better (smaller) middle candidate
            else:
                return True        # n > second > (some earlier) first

        return False
