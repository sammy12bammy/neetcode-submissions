class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort in arr
        nums.sort()

        # iterate through index and value
        for i, a in enumerate(nums):
            if a > 0:
                break
            # i isnt first value and not the same as last number
            if i > 0 and a == nums[i-1]:
                continue
            
            # 2 sum
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                	r -= 1
                elif threeSum < 0:
                	l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # dont want the same sum
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        # same value
                        l += 1
        return res