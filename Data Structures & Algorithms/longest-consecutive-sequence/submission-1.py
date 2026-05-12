class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if (num-1) not in s:
                l = 1
                while (num + l) in s:
                    l += 1
                longest = max(longest, l)
        return longest