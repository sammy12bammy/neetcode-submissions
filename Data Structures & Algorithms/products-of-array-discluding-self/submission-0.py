class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        l = len(nums)
        r = []
        for i in range(l):
            prod = 1
            for j in range(l):
                if i != j:
                    prod = prod * nums[j]
            r.append(prod)
        return r