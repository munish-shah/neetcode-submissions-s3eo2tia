class Solution:
    def spiralOrder(self, row: List[List[int]]) -> List[int]:
        # O(m * n)
        res = []
        left, right, top, bottom = 0, len(row[0]), 0, len(row)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(row[top][i])
            top += 1

            for i in range (top, bottom):
                res.append(row[i][right - 1])
            
            right -= 1

            if not (left < right and top < bottom):
                break
            
            for i in range(right - 1, left - 1, -1):
                res.append(row[bottom - 1][i])
            
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(row[i][left])
            
            left += 1

        return res
            


