class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //=10
            return digit_sum

        dict = defaultdict(list)
        for num in nums:
            digit_sum = get_digit_sum(num)
            dict[digit_sum].append(num)

        # print(dict)
        ans = -1
        for key in dict:
            curr = dict[key]
            print(curr)
            if len(curr) > 1:
                curr.sort(reverse=True)
                print(curr)
                ans = max(ans, curr[0] + curr[1])

        return ans