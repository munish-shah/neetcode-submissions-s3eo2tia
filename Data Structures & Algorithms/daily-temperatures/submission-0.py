class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [73,74,75,71,69,72,76,73]
        stack_idx = []
        answers = [0] * len(temperatures)
        x = 1
        for idx, temp in enumerate(temperatures):
    
            while stack and temp > stack[-1]:
                    stack.pop()
                    answers[stack_idx[-1]] = idx - stack_idx[-1]
                    stack_idx.pop()

            stack.append(temp)
            stack_idx.append(idx)

        return answers

