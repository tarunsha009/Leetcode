class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])
#         a = 0
#         for i in range(len(nums)):
#             a = a + nums[i]
#             nums[i] = a
        
        return prefix_sum

