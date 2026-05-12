class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        largest = nums[len(nums)-1]

        for n in nums:
            res[n] += 1
        
        ret = []
        # find the k largest in the res dict
        sortDic = dict(sorted(res.items(), key=lambda x:x[1], reverse = True))

        for key in list(sortDic.keys())[:k]:
            ret.append(key)
        return ret