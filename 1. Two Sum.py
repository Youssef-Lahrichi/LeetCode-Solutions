class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] not in seen.keys():
                seen[nums[i]] = i
            else:
                return [seen[target - nums[i]], i]
