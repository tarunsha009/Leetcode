class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0] * (len(gain) + 1)
        highest = prefix[0]
        for i in range(len(gain)):
            prefix[i + 1] = gain[i] + prefix[i]
            highest = max(highest, prefix[i + 1])

        return highest

        