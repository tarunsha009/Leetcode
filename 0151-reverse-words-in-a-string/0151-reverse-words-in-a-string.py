class Solution:
    def reverseWords(self, s: str) -> str:
        # abc = list(s.strip().split(' '))
        # abc = [x for x in abc if x != ""]
        # new_ls = abc[::-1]
        # return " ".join(new_ls)
        abc = s.split()
        print(abc)
        return " ".join(reversed(abc))