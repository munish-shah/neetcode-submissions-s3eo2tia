class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()

        for x in nums:
            if x in duplicates:
                return True
            else:
                duplicates.add(x)
        return False