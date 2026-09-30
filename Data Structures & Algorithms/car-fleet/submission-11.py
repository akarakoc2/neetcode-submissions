class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_pairs = sorted(zip(position, speed), reverse = True)
        sorted_pos, sorted_speed = map(list, zip(*sorted_pairs))
        
        stack = []

        for i in range(len(sorted_pos)):
            time = (target - sorted_pos[i]) / sorted_speed[i]
            while stack and stack[-1] < time:
                stack.append(time)
            if i == 0:
                stack.append(time)
        return len(stack)