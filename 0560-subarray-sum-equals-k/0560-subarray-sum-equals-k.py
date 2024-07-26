class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = defaultdict(int)
        sum = count = 0
        map[0] = 1

        for n in nums:
            sum += n
            count += map[sum - k]
            map[sum] +=1
        
        return count

        