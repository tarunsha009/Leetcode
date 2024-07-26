class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str in strs:
            result["".join(sorted(str))].append(str)

        return list(result.values())
        