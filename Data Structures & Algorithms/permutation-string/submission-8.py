from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:   
        if len(s1) > len(s2):
            return False
		    
        count = Counter(s1)
        need = len(count)
        have = 0
        l = 0

        for r, c in enumerate(s2):
            count[c] -= 1

            if count[c] == 0:
                have += 1

            if r - l + 1 > len(s1):
                if count[s2[l]] == 0:
                    have -= 1

                count[s2[l]] += 1
                l += 1

            if need == have:
                return True

        return need == have