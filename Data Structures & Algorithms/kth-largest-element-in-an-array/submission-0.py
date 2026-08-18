class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-1 * nums[i] for i in range(len(nums))]
        heapq.heapify(nums)

        counter = 1
        while counter != k:
            heapq.heappop(nums)
            counter += 1

        return -1 * nums[0]
        