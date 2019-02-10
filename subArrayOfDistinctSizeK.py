# # # # -*- coding: utf-8 -*-
"""
Given an array of letters and a window size k, return
subarrays of size k with no duplicates.
e.g. [a, d, f, g, k, g] and window size k = 4
return [[a, d, f, g], [d, f, g, k]]
"""
def subArrayWithKDistinct(array, k):
    result = []
    for i in range(0, len(array)-k+1):
        size_k_subarray = array[i:i+k]
        if checkDistinctCharNum(size_k_subarray, k):
            result.append(size_k_subarray)
    return result

def checkDistinctCharNum(array, k):
    temp = {}
    for c in array:
        if c not in temp:
            temp[c] = 0
        temp[c] += 1
        if temp[c] > 1:
            return False
    return True

if __name__ == '__main__':
    array = ['a', 'd', 'f', 'g', 'k', 'g']
    k = 4
    print(subArrayWithKDistinct(array,k))