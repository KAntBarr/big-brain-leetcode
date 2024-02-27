class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        curSet = []
        i = 0
        self.helper(i, nums, subsets, curSet)
        return subsets

    def helper(self, i, nums, subsets, curSet):
        # base case that checks if the current index
        # is outside of the array or at the end of it
        if i >= len(nums):
            # if true add a copy of the current set
            # to the list of subsets
            subsets.append(list(curSet))
            return
        
        # branch into the next index without the current number
        self.helper(i+1, nums, subsets, curSet)

        # add the current number to the current set
        curSet.append(nums[i])

        # branch into the index with the added current number
        self.helper(i+1, nums, subsets, curSet)

        curSet.pop()