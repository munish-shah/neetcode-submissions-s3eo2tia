class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target > row[-1]:
                continue
            
            start = 0
            end = len(row) - 1

            while start <= end:
                mid = (start + end) // 2


                if row[mid] < target:
                    start = mid + 1

                elif row[mid] > target:
                    end = mid - 1

                elif target == row[mid]:

                    return True
            
            return False
        return False