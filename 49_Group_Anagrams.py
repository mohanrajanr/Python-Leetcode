# # # # -*- coding: utf-8 -*-

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        for str_item in strs:
            sorted_str = ''.join(sorted(str_item))
            # 注意这里写复杂了 看下面能通过的逻辑的写法!
            # if sorted_str in str_dict.keys(): # No need to use hash function!
            #     str_dict[sorted_str].append(str_item)
            # else:
            #     l = []
            #     l.append(str_item)
            #     str_dict[sorted_str] = l

            # 能通过的逻辑的写法
            if not str_dict.has_key(sorted_str):
                str_dict[sorted_str] = []
            str_dict[sorted_str].append(str_item)
        result = []
        # dict.items() returns a list of 2-tuples ([(key, value), (key, value), ...]), whereas dict.iteritems()
        for key, item in str_dict.items():
            result.append(sorted(item))
        return result

if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s.groupAnagrams(strs)