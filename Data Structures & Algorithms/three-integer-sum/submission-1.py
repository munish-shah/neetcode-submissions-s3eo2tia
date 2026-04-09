class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)

        a = 0
        res = []
        for x in range(len(arr) - 1):
            l = x + 1
            r = len(arr) - 1
            if x > 0 and arr[x] == arr[x-1]:
                continue
            while l < r:
                if arr[x] + arr[l] + arr[r] == 0:
                    res.append([arr[x], arr[l], arr[r]])
                    l += 1
                    while arr[l] == arr[l-1] and l < r:
                        l += 1
                elif arr[x] + arr[l] + arr[r] > 0:
                    r -= 1
                elif arr[x] + arr[l] + arr[r] < 0:
                    l += 1
                
        return res

            