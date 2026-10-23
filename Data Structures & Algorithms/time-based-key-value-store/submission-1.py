class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyStore:
            self.keyStore[key].append([value, timestamp])
        else:
            self.keyStore[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])
        # values contains list of lists [[h, 1], [s, 2], [a, 3]]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = str(values[m][0])
                l = m + 1
            else:
                r = m - 1
        return res
                
