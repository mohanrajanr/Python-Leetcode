# # # # -*- coding: utf-8 -*-
class Solution(object):
    # def totalFruit(self, tree):
    #     """
    #     :type tree: List[int]
    #     :rtype: int
    #     """
    #     max_length = 0
    #     start = 0
    #     for i in range(0, len(tree)-1):
    #         num_of_types = set()
    #         num_of_types.add(tree[i])
    #         for j in range(i+1, len(tree)):
    #             num_of_types.add(tree[j])
    #             current_result = j - i + 1
    #             if len(num_of_types) > 2:
    #                 current_result = j - i
    #                 max_length = max(max_length, current_result)
    #                 break
    #             else:
    #                 current_result = j - i + 1
    #                 max_length = max(max_length, current_result)
    #     return max_length

    def totalFruit(self, tree):
        count = {}
        i = res = 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res

if __name__ == '__main__':
    s = Solution()
    tree = [3,3,3,1,2,1,1,2,3,3,4]
    assert s.totalFruit(tree) == 5
    # tree = [1,2,1]
    # assert s.totalFruit(tree) == 3
    # tree = [0,1,2,2]
    # assert s.totalFruit(tree) == 3
    # tree = [1,2,3,2,2]
    # assert s.totalFruit(tree) == 4
