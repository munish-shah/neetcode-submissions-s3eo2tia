class Solution:
    def isValid(self, s: str) -> bool:
        open_p = []
        close_p = []
        d = {"]": "[", "}": "{", ")": "("}
        for x in s:
            if x in "[{(":
                open_p.append(x)
            elif x in "]})" and open_p:
                if d[x] == open_p[-1]:
                    open_p.pop()
                else:
                    return False
            else: return False
        if open_p:
            print(open_p)
            return False
        return True
