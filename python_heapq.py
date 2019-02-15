# # # # -*- coding: utf-8 -*-

import heapq

if __name__ == '__main__':
    # https://blog.csdn.net/JNingWei/article/details/78493636
    origin_list = [1, 3, 5, 2, 4, 6, 0]
    sorted_list = [0, 1, 2, 3, 4, 5, 6]

    import heapq # 注意是 小顶堆 噢～

    # heapify接口 等于循环把list中的元素 push入 堆
    import copy
    h = copy.copy(origin_list)
    heapq.heapify(h)
    assert h == [0, 2, 1, 3, 4, 6, 5] != origin_list

    # 也可以自己 手动 一个一个元素 push进 堆
    h = []
    for item in origin_list:
        heapq.heappush(h, item)

    # 堆 本身依然是 list
    assert type(h) == list

    # 每 pop 一次，该小顶堆就会重新 堆排序 一次
    assert h == [0, 2, 1, 3, 4, 6, 5] != origin_list != sorted_list
    h = [heapq.heappop(h) for _ in xrange(len(h))]
    assert h == sorted_list
