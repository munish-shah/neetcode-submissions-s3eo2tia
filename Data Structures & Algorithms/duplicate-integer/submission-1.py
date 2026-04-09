class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # hashnums = {}
        # for index, x in enumerate(nums):
            
        #     if x in hashnums:
        #         return True
        #     hashnums[x] = index
        # return False
        return len(set(nums)) < len(nums)
         