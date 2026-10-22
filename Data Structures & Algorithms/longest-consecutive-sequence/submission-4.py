class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        r = 0

        for n in s:
            if n - 1 not in s:
                c = 1
                while n + c in s:
                    c += 1
                r = max(r, c)

        return r