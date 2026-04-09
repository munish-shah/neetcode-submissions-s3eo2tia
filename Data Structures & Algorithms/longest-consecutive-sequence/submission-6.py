class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        print(nums)
        consecutive = 1
        prev = nums[0]
        longest_seq = 1
        for x in nums:
            if prev == x:
                prev = x
                continue
            elif prev + 1 == x:
                print(prev, x)
                consecutive += 1
            else:
                consecutive = 1
            longest_seq = max(longest_seq, consecutive)
            prev = x
        return longest_seq
            

