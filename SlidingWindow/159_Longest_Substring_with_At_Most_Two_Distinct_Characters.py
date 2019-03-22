# # # # -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int

        Return N if the string length N is smaller than 3.
        Set both set pointers in the beginning of the string left = 0 and right = 0
        and init max substring length max_len = 2.

        While right pointer is less than N:
        If hashmap contains less than 3 distinct characters, add the current character s[right] in the hashmap and move right pointer to the right.
        If hashmap contains 3 distinct characters, remove the leftmost character from the hashmap and move the left pointer so that sliding window contains again 2 distinct characters only.
        Update max_len.
        """
        if len(s) < 3:
            return len(s)
        max_len = 2
        left = right = 0
        hashmap = {}
        while right < len(s):
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1
            if len(hashmap) == 3:
                # {'l': 0, 'e': 7, 't': 8}
                min_index = min(hashmap.values())
                min_index_char = s[min_index]
                del hashmap[min_index_char]
                while left <= min_index:
                    left += 1
            max_len = max(right-left, max_len)
        return max_len


if __name__ == '__main__':
    s = Solution()
    text = 'leeeeeeeetcooooooooode'
    print(s.lengthOfLongestSubstringTwoDistinct(text))
