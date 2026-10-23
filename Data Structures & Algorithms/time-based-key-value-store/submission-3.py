class TimeMap:

    def __init__(self):
        self.HashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.HashMap:
            self.HashMap[key].append([value, timestamp])
        else:
            self.HashMap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        # our aim with this get function is to get 
        # the most recent value for latest timestamp

        # since we know the key we can say that the value 
        # of the key as
        values = self.HashMap.get(key, [])
        # values = [['happy', 2], ['sad', 3]]

        # now we need to pointers to perform binary search on this values
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2 
            if values[m][1] <= timestamp:        
                res = str(values[m][0])
                l = m + 1
            else:
                r = m - 1
        return res