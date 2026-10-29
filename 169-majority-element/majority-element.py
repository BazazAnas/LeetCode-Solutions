class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #solution using a dict
        # d = {}

        # for n in nums:
        #     d[n] = d.get(n,0) + 1
        #     if(d[n] > len(nums) / 2):
        #         return n


        maxi = 0
        c = 0

        for i in nums:
            if c == 0:
                maxi = i
                c += 1
            elif i == maxi:
                c += 1
            else:
                c -= 1
            
        return maxi



