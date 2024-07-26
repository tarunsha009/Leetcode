class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}
        for winner, losser in matches:
            loss_count[winner] = loss_count.get(winner, 0)
            loss_count[losser] = loss_count.get(losser, 0) + 1

        print(loss_count)
        zero_loss, one_loss = [], []
        for player, count in loss_count.items():
            if count == 0:
                zero_loss.append(player)
            elif count == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]
        