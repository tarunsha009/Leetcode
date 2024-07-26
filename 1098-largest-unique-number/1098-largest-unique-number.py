class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        print(count)
        largest = -1
        for key, val in count.items():
            if val == 1:
                largest = max(largest, key)

        return largest
        