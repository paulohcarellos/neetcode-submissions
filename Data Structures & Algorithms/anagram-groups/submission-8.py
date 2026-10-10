class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            fa = [0] * 26

            for c in s:
                fa[ord(c) - ord('a')] += 1

            groups[tuple(fa)].append(s)

        return list(groups.values())