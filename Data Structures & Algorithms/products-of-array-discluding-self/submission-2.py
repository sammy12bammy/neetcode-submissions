class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1] * (len(nums))

        pre = 1
        for i in range(len(nums)):
            r[i] = pre # store prefixes in res out arr
            pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            r[i] *= post
            post *= nums[i]
        return r
        