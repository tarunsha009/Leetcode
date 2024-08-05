class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        for idx, val in enumerate(l):
            l[idx] = val[::-1]
        
        return " ".join(l)

        