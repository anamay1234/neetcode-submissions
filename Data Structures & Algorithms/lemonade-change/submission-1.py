class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = {}
        hashmap[5] = 0
        hashmap[10] = 0
        hashmap[20] = 0

        change = 0

        for bill in bills:
            hashmap[bill] += 1

            if bill == 5:
                continue
            if bill == 10:
                if hashmap[5] > 0:
                    hashmap[5] -= 1
                else:
                    return False
            if bill == 20:
                if hashmap[10] > 0 and hashmap[5] > 0:
                    hashmap[10] -= 1
                    hashmap[5] -= 1
                elif hashmap[5] >= 3:
                    hashmap[5] -= 3
                else:
                    return False
                    
        return True

                

        