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


if __name__ == '__main__':
    lst = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    lst = [[1, 3], [-2, 2]]
    k = 1
    print (topKClosestToOrigin(lst, k))