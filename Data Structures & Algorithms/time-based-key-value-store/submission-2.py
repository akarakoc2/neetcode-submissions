class TimeMap:
    def __init__(self):
        self.timeMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([value,  timestamp])
        else:
            self.timeMap[key] = [[value, timestamp]]
            
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        l,r = 0, len(self.timeMap[key]) - 1
        valid_ans = ""
        while l <= r:
            mid = (l + r) // 2

            if self.timeMap[key][mid][1] == timestamp:
                return self.timeMap[key][mid][0]
            elif self.timeMap[key][mid][1] < timestamp:
                valid_ans = self.timeMap[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return valid_ans 
            
        




        

        
