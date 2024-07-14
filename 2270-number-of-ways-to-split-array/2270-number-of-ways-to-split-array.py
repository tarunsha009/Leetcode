class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        partition = 0
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])

        print(prefix_sum)
        for i in range(len(nums)-1):
            if prefix_sum[i] >=  prefix_sum[-1] - prefix_sum[i]:
                partition +=1

        return partition
        