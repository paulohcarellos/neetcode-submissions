class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]):
        st = []
        ps = sorted(zip(position, speed), key=lambda x: x[0])

        for pos, spd in ps:
            st.append((target - pos) / spd)

        fleets = 0

        while st:
            front = st.pop()
            fleets += 1

            while st and st[-1] <= front:
                st.pop()

        return fleets