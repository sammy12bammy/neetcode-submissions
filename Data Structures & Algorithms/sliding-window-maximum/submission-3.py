class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use deque
        out = []
        q = deque() # indices
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # while smaller numbers exist in queue
                q.pop()
            q.append(r)
            # if left oob remove left val from window
            if l> q[0]:
                q.popleft()
            
            if (r+1) >= k:
                out.append(nums[q[0]])
                l += 1
            r += 1
        return out
