class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key] = self.hashmap.get(key, [])
        self.hashmap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hashmap:
            return ""

        L = 0
        R = len(self.hashmap[key]) - 1

        while L <= R:
            M = (L + R) // 2
            if self.hashmap[key][M][0] == timestamp:
                return self.hashmap[key][M][1] 
            elif self.hashmap[key][M][0] > timestamp:
                R = M - 1
            elif self.hashmap[key][M][0] < timestamp:
                L = M + 1

        if R < 0:
            return ""
        else:
            return self.hashmap[key][R][1] 
    
        
        
