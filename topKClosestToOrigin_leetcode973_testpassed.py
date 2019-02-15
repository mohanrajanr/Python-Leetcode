# -*- coding: utf-8 -*-

def topKClosestToOrigin(lst, k):
    """
    Given a list of points on the 2-D plane and an integer K. The task is to find K closest points to the origin and print them.
    Note: The distance between two points on a plane is the Euclidean distance.
    Examples:
    Input : point = [[3, 3], [5, -1], [-2, 4]], K = 2
    Output : [[3, 3], [-2, 4]]

    Input : point = [[1, 3], [-2, 2]], K  = 1
    Output : [[-2, 2]]

    :param lst: list[list[int]]
    :param k: int
    :return: list[list[int]]
    """
    for l in lst:
        l.append(l[0]**2+l[1]**2)
    lst.sort(key=lambda x:x[2])

    for l in lst:
        l.pop()
    return lst[0:k]


# if __name__ == '__main__':
    # lst = [[3, 3], [5, -1], [-2, 4]]
    # k = 2
    # lst = [[1, 3], [-2, 2]]
    # k = 1
    # print (topKClosestToOrigin(lst, k))

# Time complexity is O(Nlog(K)) ?




# if __name__ == '__main__':
#     points = [[4,6],[4,6],[4,6],[-4,-6],[-4,6]]
#     origin = [0,0]
#     k = 3
#
#     s = Solution()
#     s.kClosest(points, origin, k)






# lintcode 612
import heapq
class Solution:
    # method1: use heapq's nsmallest function and lambda expression
    # def kClosest(self, points, o, k):
    #     return heapq.nsmallest(k, points, key=lambda p: [(p.x-o.x)**2 + (p.y-o.y)**2, p.x])

    # method2: use minheap
    def kClosest(self, points, o, k):
        heap_dis, res, dis2points = [], [], {}
        # heap_dis stores the min heap
        # 0th element is the smallest, 1th and 2nd elements are 0th's child, 3th and 4th are 1th child, etc.

        # build dis2points map
        for p in points:
            d = (p[0]-o[0])**2 + (p[1]-o[1])**2
            if d not in dis2points:
                dis2points[d] = [p]
                heapq.heappush(heap_dis, d)
            else:
                dis2points[d].append(p)

        # find kth closest
        while len(res) < k:
            d = heapq.heappop(heap_dis) # pop the smallest from heap
            if len(dis2points[d]) + len(res) <= k:
                # sort points by x, version1
                res += sorted(dis2points[d], key=lambda p: p[0])
            else:
                # sort points by x, version2
                x_heap, x2point = [], {}
                for p in dis2points[d]:
                    x2point[p[0]] = p
                    heapq.heappush(x_heap, p[0])
                while len(res) < k:
                    x = heapq.heappop(x_heap)
                    res += [x2point[x]]
        return res

points = [[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],[-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],[60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]]
o = [100, 71]
k = 10
s = Solution()
s.kClosest(points, o, k)