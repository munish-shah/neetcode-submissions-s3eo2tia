class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [73,74,75,71,69,72,76,73]
        answers = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
    
            while stack and temp > temperatures[stack[-1]]:
                    answers[stack[-1]] = idx - stack[-1]
                    stack.pop()

            stack.append(idx)

        return answers

