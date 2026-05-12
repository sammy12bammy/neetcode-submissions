class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = set(nums)
        if len(nums1) == len(nums):
            return False
        else:
            return True