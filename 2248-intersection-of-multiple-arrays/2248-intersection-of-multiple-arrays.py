from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        for arr in nums:
            for n in arr:
                count[n] +=1

        result = []
        for key in count:
            if count[key] == len(nums):
                result.append(key)

        return sorted(result) 