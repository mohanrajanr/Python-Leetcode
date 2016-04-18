# # # # -*- coding: utf-8 -*-
# Definition for an interval.
# 此题关键点:
# 1. 要排序后再做 - 怎么对List[List]排序?
# 2. 排序后,第1,2个合并完,如果merge成一个则继续和第3个合并,如果不能merge则第1,2个没有overlap, 则第3个和第一个也没有overlap
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        sorted_intervals = self.sortintervals(intervals)
        # for i in sorted_intervals:
        #     print i.start, i.end
        result = []
        i = 1
        if not intervals:
            return result

        curr_interval = sorted_intervals[0]
        result.append(curr_interval)
        while i < len(intervals):
            if self.checkifoverlap(curr_interval, sorted_intervals[i]):
                result.pop()
                temp = Interval(s=min(curr_interval.start, sorted_intervals[i].start),
                                e=max(curr_interval.end, sorted_intervals[i].end))
                result.append(temp)
                curr_interval = temp
            else:
                result.append(sorted_intervals[i])
                curr_interval = sorted_intervals[i]
            i += 1
        return result

    def checkifoverlap(self, i1, i2):
        if i1.start > i2.end or i2.start > i1.end:
            return False
        else:
            return True

    def sortintervals(self, list_intervals):
        import operator
        return sorted(list_intervals, key=operator.attrgetter('start'))

if __name__ == '__main__':
    s = Solution()
    # i1 = Interval(1,2)
    # i2 = Interval(4,6)
    # i3 = Interval(4,5)
    # i4 = Interval(2,3)
    #[1,3],[2,6],[8,10],[15,18]
    i1 = Interval(1,3)
    i2 = Interval(8,10)
    i3 = Interval(15,18)
    i4 = Interval(2,6)
    list_intervals = []
    list_intervals.append(i1)
    list_intervals.append(i2)
    list_intervals.append(i3)
    list_intervals.append(i4)
    #print s.checkIfOverlap(i1,i2)
    # sorted_list = s.sortintervals(list_intervals)
    # for i in sorted_list:
    #     print i.start, i.end
    merged_list = s.merge(list_intervals)
    for i in merged_list:
         print i.start, i.end