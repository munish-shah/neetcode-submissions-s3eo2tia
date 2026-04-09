class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for x in range(len(nums)):
            if (target - nums[x]) in num_dict:
                return [num_dict[target - nums[x]], x]
            else:
                num_dict[nums[x]] = x
        