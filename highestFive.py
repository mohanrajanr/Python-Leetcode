# # # # -*- coding: utf-8 -*-
"""
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
每人至少有5份成绩，要取最高的5份的average
"""
def highestFive(array):
    result = {}
    for s in array:
        if s[0] not in result:
            result[s[0]] = []
        result[s[0]].append(s[1])
    for key,value in result.iteritems():
        # list.sort mutates the list in-place & returns None
        # sorted takes any iterable & returns a new list, sorted.

        value.sort(reverse=True)
        value = value[0:5]
        print key , value
        result[key] = sum(value)/5.0
    print(result)
    return result

if __name__ == '__main__':
    array = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61],[1,100]]
    highestFive(array)
