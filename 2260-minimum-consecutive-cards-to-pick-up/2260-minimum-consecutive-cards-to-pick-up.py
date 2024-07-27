class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = {}
        start = 0
        ans = float("inf")
        for end in range(len(cards)):
            value = cards[end]
            count[value] = count.get(value , 0) + 1
            while count[value] > 1:
                count[cards[start]] -=1
                ans = min(ans, end - start + 1)
                start +=1

            # ans = min(ans, end - start)

        return ans if ans < float("inf") else -1
        