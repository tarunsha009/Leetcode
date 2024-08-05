class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        max_len = float("-inf")
        for idx in range(1, len(nums)):
            if nums[idx-1] < nums[idx]:
                count +=1
                max_len = max(max_len, count)
            else:
                max_len = max(max_len, count)
                count = 1

        return max_len
        