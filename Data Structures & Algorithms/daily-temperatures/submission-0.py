class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize the array with 0s
        stack = []        # This will store indices of the temperatures
        
        for i in range(n):
            # Check if current temperature is warmer than the temperature at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index  # Calculate the days waited
                
            stack.append(i)  # Push the current day's index onto the stack
            
        return result
