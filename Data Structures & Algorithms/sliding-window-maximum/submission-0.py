class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        ans = []

        for i in range(len(nums)):

            # Remove indices outside the window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove indices whose values are smaller
            # than the current value
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # Window has reached size k
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans



        