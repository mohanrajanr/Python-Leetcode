# # # # -*- coding: utf-8 -*-
import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        # minimum_wage = float('inf')
        # for worker in range(len(quality)):
        #     heap = []
        #     current_wage = wage[worker]
        #     current_ratio = current_wage / float(quality[worker])
        #     for i in range(len(quality)):
        #         i_wage = current_ratio * quality[i]
        #         if i_wage >= wage[i]:
        #             heapq.heappush(heap, 0-i_wage)
        #         if len(heap) > K:
        #             heapq.heappop(heap)
        #     if len(heap) == K:
        #         salaries = [-x for x in heap]
        #         minimum_wage = min(minimum_wage, sum(salaries))
        # return minimum_wage
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q) # heap stores the quality, not the total amount
            qsum += q
            if len(heap) > K:
                last = heapq.heappop(heap) # For the current ratio, this will generate the biggest amount
                qsum += last # because this is a negative number, use qsum +=
            if len(heap) == K:
                res = min(res, qsum * r)
        return res

if __name__ == '__main__':
    s = Solution()
    # quality = [10, 20, 5]
    # wage = [70, 50, 30]
    # K = 2
    quality = [3,1,10,10,1]
    wage = [4,8,2,2,7]
    K = 3
    print(s.mincostToHireWorkers(quality, wage, K))
