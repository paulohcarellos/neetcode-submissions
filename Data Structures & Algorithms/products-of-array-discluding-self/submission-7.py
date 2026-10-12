from math import prod

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zeros = nums.count(0)
        if zeros > 1:
            return [0] * len(nums)

        total = prod(n for n in nums if n)
        if zeros == 1:
            return [0 if n else total for n in nums]

        return [total // n for n in nums]