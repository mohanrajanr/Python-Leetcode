# # # # -*- coding: utf-8 -*-
"""
Given a string and a number k. Find all sub strings of size k with k distinct characters.
Example:
input: abcdkeewrf and 4
[0], [9]
output: abcd, bcdk, cdke,ewrf
"""
def substringWithKDistinct(str, k):
    result = []
    for i in range(0, len(str)-k+1):
        size_k_substring = str[i:i+k]
        if checkDistinctCharNum(size_k_substring, k):
            result.append(size_k_substring)
    return result

def checkDistinctCharNum(str, k):
    temp = {}
    for c in str:
        if c not in temp:
            temp[c] = 0
        temp[c] += 1
        if temp[c] > 1:
            return False
    return True

if __name__ == '__main__':
    str = "abcdkeewrf"
    size = 4
    print(substringWithKDistinct(str, size))

# substring whose size is k