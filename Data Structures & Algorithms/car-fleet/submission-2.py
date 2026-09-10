class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_pairs = sorted(zip(position, speed),reverse = True)
        sorted_position, sorted_speed = map(list, zip(*sorted_pairs))

        stack = []
        for i in range(len(sorted_position)):
            time = (target - sorted_position[i]) / sorted_speed[i]
            while stack and stack[-1] < time:
                stack.append(time)

            if i == 0:
                stack.append(time)
                
        return len(stack)
    
        
                    