# # # # -*- coding: utf-8 -*-
# Definition for an interval.
# 算法: 从intervals第0个开始check是否intervals[i]和newInterval overlap
# 如果没有overlap则继续向前 如果有 则要从此处开始merge 然后check从当前i往后的每个元素是否都有overlap
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        if not intervals:
            return [newInterval]

        i = 0
        while i < len(intervals):
            # 如果没有overlap
            if not self.checkifoverlap(newInterval, intervals[i]):
                result.append(intervals[i])
                i += 1
            # 如果有overlap
            else:
                break

        if i == len(intervals):
            result = []
            j = 0
            new_interval_inserted = False
            while j < len(intervals):
                if intervals[j].start < newInterval.start:
                    result.append(intervals[j])
                elif intervals[j].start > newInterval.start:
                    result.append(newInterval)
                    new_interval_inserted = True
                    #result.append(intervals[j])
                    break
                j += 1
            if new_interval_inserted:
                result.extend(intervals[j:])
            if not new_interval_inserted:
                result.append(newInterval)
            return result

        curr_interval = intervals[i]
        temp = Interval(s=min(curr_interval.start, newInterval.start),
                        e=max(curr_interval.end, newInterval.end))
        result.append(temp)
        i += 1
        curr_interval = result[-1]
        #print curr_interval.start, curr_interval.end

        while i < len(intervals):
            if self.checkifoverlap(curr_interval, intervals[i]):
                result.pop()
                temp = Interval(s=min(curr_interval.start, intervals[i].start),
                                e=max(curr_interval.end, intervals[i].end))
                result.append(temp)
                curr_interval = temp
            else:
                result.append(intervals[i])
                curr_interval = result[-1]
            i += 1
        return result

    def checkifoverlap(self, i1, i2):
        if i1.start > i2.end or i2.start > i1.end:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    #[[0,2],[3,5],[6,8],[10,12],[13,15]]
    i1 = Interval(0,2)
    i2 = Interval(3,5)
    i3 = Interval(6,8)

    list_intervals = []
    list_intervals.append(i1)
    list_intervals.append(i2)
    list_intervals.append(i3)
    newInterval = Interval(4,7)

    i1 = Interval(2,5)
    i2 = Interval(8,13)
    i3 = Interval(14,16)
    list_intervals = []
    list_intervals.append(i1)
    list_intervals.append(i2)
    list_intervals.append(i3)

    newInterval = Interval(0,1)
    # newInterval = Interval(6,6)

    inserted = s.insert(list_intervals, newInterval)
    for i in inserted:
        print i.start, i.end