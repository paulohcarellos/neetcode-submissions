from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        most_freq = 0
        res = 0
        l = 0

        for r, c in enumerate(s):
            count[c] += 1
            most_freq = max(most_freq, count[c])

            if r - l + 1 - most_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

                


            