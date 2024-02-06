class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return nums[0]

        returnVal = 0
        for num in nums:
            returnVal = returnVal ^ num

        return returnVal