class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        hours = lambda s: sum((p + s - 1) // s for p in piles)

        while l < r:
            m = (l + r) // 2
            t = hours(m)

            if t > h:
                l = m + 1
            else:
                r = m

        return l