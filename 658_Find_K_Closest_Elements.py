# # # # -*- coding: utf-8 -*-
def findClosestElements(array, k, x):
    # http://www.cnblogs.com/grandyang/p/7519466.html
    left, right = 0, len(array) - k
    while left < right:
        mid = (left + right) / 2
        if x - array[mid] > array[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return array[left:left + k]

if __name__ == '__main__':
    arr = [0,1,1,1,2,3,6,7,8,9]
    k = 5
    x = 4
    print(findClosestElements(arr, k, x))
