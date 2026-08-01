class TimeMap:

    def __init__(self):
       self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value, timestamp))
        return None

    def get(self, key: str, timestamp: int) -> str:
        val = self.m[key]

        if not val: return ""

        l, r = 0, len(val)-1
        mid = 0
        while l <= r:
            mid = (l+r)//2
            _, t = val[mid]
            if t == timestamp:
                return val[mid][0]
            elif timestamp > t:
                l = mid + 1
            else:
                r = mid - 1

        if val[mid][1] > timestamp and mid > 0:
            return val[mid-1][0]
        elif val[mid][1] <= timestamp:
            return val[mid][0]
        
        return ""