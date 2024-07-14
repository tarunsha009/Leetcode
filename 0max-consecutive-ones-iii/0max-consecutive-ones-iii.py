class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0;
        ans = 0
        zero_count = 0
        # current_size = 0
        for end in range(len(nums)):
            value = nums[end]
            if value == 0 and zero_count == k:
                while zero_count == k:
                    if nums[start] == 0:
                        zero_count -=1
                    start += 1

                # current_size = 1
                # zero_count = 1
                # continue
            if value == 0 and zero_count < k:
                zero_count +=1

            current_size = end - start +1
            ans = max(current_size, ans)

        return ans
        