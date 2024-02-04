class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) / 2
            # print('left:', left, 'right:', right, 'middle:', middle)
            if nums[middle] == target: return middle
            if nums[middle] < target:
                left = middle + 1
            if nums[middle] > target:
                right = middle - 1

        # print("couldn't find a match")
        return -1