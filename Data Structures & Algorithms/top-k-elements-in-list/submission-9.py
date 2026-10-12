from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        buckets = [[] for _ in range(max(c.values()) + 1)]
        
        for num, freq in c.items():
            buckets[freq].append(num)

        res = []
        for b in reversed(buckets):
            res.extend(b)

            if len(res) >= k:
                return res[:k]