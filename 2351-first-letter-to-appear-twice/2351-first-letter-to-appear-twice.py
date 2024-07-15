class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for item in s:
            if item in seen:
                return item
            else:
                seen.add(item)
        return ""
        