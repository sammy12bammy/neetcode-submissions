class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        look = {}
        for i,n in enumerate(nums):
            look[n] = i
        
        for i, n in enumerate(nums):
            dif = target - n
            if dif in look and look[dif] != i:
                return [i, look[dif]]
        return []