class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        l = 0
        res = 0
        for i, c in enumerate(s):
            if c in h and h[c] >= l:
                l = h[c] + 1
            h[c] = i
            res = max(res, i - l + 1)
        return res