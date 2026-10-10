class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = {}
        op = 0

        for n in nums:
            need = k-n

            if seen.get(need , 0) > 0:
                op += 1
                seen[need] -= 1
            else:
                seen[n] = seen.get(n,0) + 1
        return op       


        