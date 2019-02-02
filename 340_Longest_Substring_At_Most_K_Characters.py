# # # # -*- coding: utf-8 -*-
class Solution:
    def countkDist(self, string_txt, k):
        """
        aaaab, k = 3, len = 5
        aaa, aaa, aab

        """
        result = []
        length = len(string_txt)
        for j in (k, length):
            for i in range(0,len(string_txt)-j+1):
                if self.checkNumOfDistinct(string_txt[i:i+j]) == k:
                    result.append(string_txt[i:i+j])
        # for i in range(0,len(string_txt)-k+1):
        #     if self.checkNumOfDistinct(string_txt[i:i+k]) == k:
        #         result.append(string_txt[i:i+k])
        return result

    def checkNumOfDistinct(self, str):
        """
        Check if string contains how many distinct characters.

        :param str:
        :param k:
        :return: int
        """
        str_dict = {}
        for c in str:
            if c not in str_dict:
                str_dict[c] = 1
            else:
                str_dict[c] += 1
        count = 0
        for k,v in str_dict.items():
            count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    string_txt = "abc"
    k = 2
    # print(s.countkDist(string_txt, k))
    print(s.countkDist(string_txt, k))

    string_txt = "aba"
    k=2
    print(s.countkDist(string_txt, k))
    string_txt = "aa"
    k=1
    print(s.countkDist(string_txt, k))
