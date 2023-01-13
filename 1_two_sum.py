class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = len(nums)
        for i in range(x):
            for j in range(x):
                if i == j:
                    continue
                if nums[i]+nums[j] == target:
                    return [i, j]
