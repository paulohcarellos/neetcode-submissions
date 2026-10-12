class Solution:

    def encode(self, strs: List[str]) -> str:
        c = len(strs)
        lens = (len(s) for s in strs)

        return ".".join(map(str, (c, *lens))) + "." + "".join(strs)

    def decode(self, s: str) -> List[str]:
        fd = s.find(".")
        splits = int(s[0:fd]) + 1

        parts = s.split(".", maxsplit=splits)
        lens = map(int, parts[1:splits])
        strs = parts[-1]

        res = []
        cut = 0

        for l in lens:
            res.append(strs[cut:cut + l])
            cut += l

        return res

