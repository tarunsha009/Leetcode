class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        start , end = 0, n-1
        
        for i in range(n-1, -1, -1):
            if abs(nums[start]) < abs(nums[end]):
                value = nums[end]
                end -=1
            else:
                value = nums[start]
                start +=1
            result[i] = value * value
        
        return result
        