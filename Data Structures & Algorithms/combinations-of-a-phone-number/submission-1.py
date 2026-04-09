class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        characMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtracking(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for x in characMap[digits[i]]:
                backtracking(i+1, curr+x)
        if digits:  
            backtracking(0, "")

        return res
