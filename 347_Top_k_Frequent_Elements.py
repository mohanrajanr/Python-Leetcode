# # # # -*- coding: utf-8 -*-
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        frequency_dict = {}
        for num in nums:
            if num not in frequency_dict:
                frequency_dict[num] = 0
            frequency_dict[num] += 1
        for k, v in frequency_dict.items():
            heapq.heappush(heap, (v, k))
        print heap
        while len(heap) > k:
            heapq.heappop(heap)
        print heap

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    s.topKFrequent(nums, k)