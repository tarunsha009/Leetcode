from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)

        return c1 == c2

        # if len(s) != len(t):
        #     return False
        # for i in s:
        #     if i in t:
        #         continue
        #     else:
        #         return False
        # return True

        