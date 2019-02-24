# # # # -*- coding: utf-8 -*-
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # the smaller half of the list, max heap
        self.large = [] # the larger half of the list, min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == len(self.large):
            smallest = -heapq.heappushpop(self.small, -num)
            heapq.heappush(self.large, smallest)
            print(self.small)
            print(self.large)
        else:
            largest = -heapq.heappushpop(self.large, num)
            heapq.heappush(self.small, largest)
            print(self.small)
            print(self.large)

    def findMedian(self):
        if not self.large:
            return 0
        if len(self.small) == len(self.large):
            return (self.small[0] + self.large[0]) / 2.0
        else:
            return self.large[0]

if __name__ == '__main__':
    m = MedianFinder()
    m.addNum(1)
    m.addNum(2)
    m.addNum(3)
    m.addNum(4)

