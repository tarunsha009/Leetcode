class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        left = 0
        
        for idx, weights in enumerate(nums):
            if  left == (total_sum - left - weights):
                return idx
            left +=weights

        return -1

        
        