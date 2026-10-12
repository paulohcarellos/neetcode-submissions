from math import prod

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        try:
            first_zero = nums.index(0)
        except ValueError:
            total = prod(nums)
            return [total // n for n in nums]

        if 0 in nums[first_zero + 1:]:
            return [0] * len(nums)
        
        total = prod([n for n in nums if n != 0])
        return [total if n == 0 else 0 for n in nums]
