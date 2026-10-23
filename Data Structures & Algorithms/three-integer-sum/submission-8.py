class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i, n in enumerate(nums):
            if n > 0:
                break
                
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                s = n + nums[l] + nums[r]

                if s == 0:
                    res.add((n, nums[l], nums[r]))
                    l += 1
                    r -= 1

                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return list(res)

