class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]:  # Reverse Sorted Order
            time = (target - p) / s

            # Only add if it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)