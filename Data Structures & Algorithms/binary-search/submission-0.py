class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            value = (end + start) // 2

            if nums[value] > target:
                end = value - 1
            elif nums[value] < target:
                start = value + 1
            elif nums[value] == target:
                return value
        return -1