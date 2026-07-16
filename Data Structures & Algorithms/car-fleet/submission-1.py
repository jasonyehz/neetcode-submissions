class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # First sort the cars from closest to finish to least
        lst = sorted(zip(position, speed), reverse = True)
        stk = []

        for x in lst:
            time = (target - x[0]) / x[1]
            if not stk or time > stk[-1]:
                stk.append(time)

        return len(stk)