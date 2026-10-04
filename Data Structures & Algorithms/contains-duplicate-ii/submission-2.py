class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        mp = {}

        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = i
                continue

            if nums[i] in mp and abs(mp[nums[i]] - i) <= k:
                print(mp[nums[i]],  i)
                return True
            else:
                mp[nums[i]] = i

        return False
            