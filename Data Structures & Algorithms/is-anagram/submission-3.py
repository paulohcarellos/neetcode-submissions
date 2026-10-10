from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)
        
        for a, b in zip(s, t):
            count[a] += 1
            count[b] -= 1

        return all(v == 0 for v in count.values())