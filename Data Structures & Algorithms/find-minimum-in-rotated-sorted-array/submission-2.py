class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the cut
        # init
        res = nums[0]
        l,r = 0, len(nums) - 1
        while l <= r:
            # if alr in valid order
            if nums[l] < nums[r]: 
                res = min(res, nums[l])
                break
            # find the mid of the splitted array
            mid = (l + r) // 2
            res = min(res, nums[mid])
            # binary search
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid -1
        return res