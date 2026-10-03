class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}

        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        arr = [[] for _ in range(len(nums) + 1)]


        for key in mp:
            arr[mp[key]].append(key)

        res = []
        count = 0

        for freq in range(len(arr) - 1, -1, -1):
            for num in arr[freq]:
                if count != k:
                    res.append(num)
                    count += 1

        return res

        



        