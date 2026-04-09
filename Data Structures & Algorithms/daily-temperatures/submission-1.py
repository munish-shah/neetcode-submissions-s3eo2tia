class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [73,74,75,71,69,72,76,73]
        answers = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
    
            while stack and temp > stack[-1][0]:
                    _, oidx = stack.pop()
                    answers[oidx] = idx - oidx

            stack.append((temp, idx))

        return answers

