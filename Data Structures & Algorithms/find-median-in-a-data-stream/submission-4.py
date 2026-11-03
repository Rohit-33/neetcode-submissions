class MedianFinder:

    def __init__(self):
        self.ar = []        

    def addNum(self, num: int) -> None:
        self.ar.append(num)
        self.ar.sort()


    def findMedian(self) -> float:
        
        if len(self.ar) %2 ==0 :
            right = len(self.ar) //2
            left = right -1

            return (self.ar[left] + self.ar[right]) / 2
        else :
            mid = len(self.ar) // 2
            return self.ar[mid]