class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)
        for x in s:
            count[x] +=1

        frequency = count.values()
        print(frequency)
        return len(set(frequency)) == 1