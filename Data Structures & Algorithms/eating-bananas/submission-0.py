class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        L = 1
        R = max(piles)

        mink = R

        while L <= R:

            k = (L + R) // 2
            # now check if u can eat all in this time

            hours = 0
            for i in range(len(piles)):
                if (piles[i] % k) == 0:
                    hours += (piles[i] // k)
                else:
                    hours += (piles[i] // k) + 1 # +1 cuz round up


            if hours <= h:
                mink = k
                print(mink, hours)
                R = k - 1
            if hours > h:
                L = k + 1

        return mink
