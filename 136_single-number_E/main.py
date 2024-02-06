class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return nums[0]

        returnSet = set()
        for num in nums:
            if num in returnSet:
                returnSet.remove(num)
            else:
                returnSet.add(num)
        
        for value in returnSet:
            return value