# # # # -*- coding: utf-8 -*-
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            return mid
    return None


if __name__ == '__main__':
    array = [i for i in range(1,5)] # 1,2,3,4 偶数个
    # array = [i for i in range(1,6)]
    target = 3
    binary_search(array, target)
