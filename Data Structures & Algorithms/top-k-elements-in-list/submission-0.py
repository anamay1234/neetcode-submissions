class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmapOfOccurances = {}

        for num in nums:
            hashmapOfOccurances[num] = hashmapOfOccurances.get(num, 0) + 1

        # key = count
        # value = array of all nums that have that count
        buckets = [[] for _ in range(len(nums) + 1)]

        for key in hashmapOfOccurances:
            buckets[hashmapOfOccurances[key]].append(key)

        array = []

        for frequency in range(len(nums), -1, -1):
            for num in buckets[frequency]:
                if k > 0:
                    array.append(num)
                    k -= 1

        return array




        