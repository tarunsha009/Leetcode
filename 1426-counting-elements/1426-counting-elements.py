class Solution:
    def countElements(self, arr: List[int]) -> int:
        new_set = set(arr)
        count = 0
        for item in arr:
            if item+1 in new_set:
                count +=1

        return count
        