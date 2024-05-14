class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        if needle == haystack:
            return 0
        
        i =0
        j = len(needle)

        while j <= len(haystack):
            current = haystack[i:j]
            if needle == current:
                return i
            i +=1
            j +=1

        return -1
            

        