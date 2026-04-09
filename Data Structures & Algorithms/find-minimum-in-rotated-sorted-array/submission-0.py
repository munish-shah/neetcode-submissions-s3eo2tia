class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        lowest = nums[0]

        while start <= end:
            if nums[start] < nums[end]:
                lowest = min(lowest, nums[start])
                break

            m = (start + end) // 2
            lowest = min(nums[m], lowest)

            if nums[m] >= nums[end]:
                start = m + 1
            else:
                end = m - 1

        return lowest