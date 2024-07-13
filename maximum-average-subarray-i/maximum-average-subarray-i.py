class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # max_avg_so_far = 0.0
        sum = 0.0
        start = 0
        if len(nums) == 1:
            return nums[0]/k

        for i in range(k):
            sum = sum + nums[i]

        avg = sum / k
        max_avg_so_far = avg
        # max_avg_so_far = max(avg, max_avg_so_far)
        for end in range(k, len(nums)):
            if end - start >= k:
                sum = sum - nums[start]
                start +=1

            sum = sum + nums[end]
            max_avg_so_far = max(max_avg_so_far, sum/k)

        return max_avg_so_far
        
        