class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i, num in enumerate(nums):
            goal = target - num
            if goal in diffs:
                return [diffs[goal], i]
            diffs[num] = i