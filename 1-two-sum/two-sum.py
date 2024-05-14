class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            total = target - nums[i]

            if total in seen:
                return [i, seen[total]]
            else:
                seen[value] = i
        