# # # # -*- coding: utf-8 -*-
import bisect

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        active = []
        """
        We'll maintain active, a sorted data structure containing every flower that has currently bloomed.
        When we add a flower to active, we should check it's lower and higher neighbors.
        If some neighbor satisfies the condition, we know the condition occurred first on this day.
        """

        for day, pos in enumerate(flowers, 1):
            i = bisect.bisect(active, pos)
            # i 代表当前pos要插入的位置
            if i-1 >= 0 and pos - active[i-1] == k + 1:
                return day
            if i < len(active) and active[i] - pos == k + 1:
                return day

            active.insert(i, pos)
        return -1

if __name__ == '__main__':
    s = Solution()
    flowers = [1,3,2]
    for day, flower in enumerate(flowers):
        print(day, flower)
        """
        0 1
        1 3
        2 2
        """
    for day, flower in enumerate(flowers, 1):
        print(day, flower)
        """
        1 1
        2 3
        3 2
        """
        # 关于enumerate:
        # def __init__(self, iterable, start=0): # known special case of enumerate.__init__
        # """ Initialize self.  See help(type(self)) for accurate signature. """
        #     pass

    # 关于python bisect的用法:
    # https://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html

    data = [2, 3, 4, 7, 9]
    print(bisect.bisect(data, 1)) # 其目的在于查找该数值将会插入的位置并返回，而不会插入。
    k = 1
    s.kEmptySlots(flowers, k)
