# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.sm, self.lg = [], []
        
    def addNum(self, num: int) -> None:
        heappush(self.sm, -1 * num)
        if (self.sm and self.lg and(-1 * self.sm[0]) > self.lg[0]):
            val = -1 * heappop(self.sm)
            heappush(self.lg, val)
        if len(self.sm) > len(self.lg)+1:
            val = -1 * heappop(self.sm)
            heappush(self.lg, val)
        if len(self.lg) > len(self.sm) +1:
            val = heappop(self.lg)
            heappush(self.sm, -1* val)

    def findMedian(self) -> float:
        # x = len(self.median_finder)//2
        if len(self.sm) > len(self.lg):
            return -1 * self.sm[0]
        elif len(self.lg) > len(self.sm):
            return self.lg[0]
        else:
            return (-1 * self.sm[0] + self.lg[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()