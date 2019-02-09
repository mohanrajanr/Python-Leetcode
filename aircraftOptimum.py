# # # # -*- coding: utf-8 -*-
def aircraftOptimum(maximumOperatingTravelDistance,
                    forwardList,
                    returnList):
    result = {}
    for f in forwardList:
        for r in returnList:
            current_cost = f[1] + r[1]
            if current_cost <= maximumOperatingTravelDistance:
                if current_cost not in result:
                    result[current_cost] = []
                result[current_cost].append([f[0],r[0]])
    result = sorted(result.iteritems(), key=lambda x: x[0], reverse=True)
    print result
    return result[0]

if __name__ == '__main__':
    maximumOperatingTravelDistance = 10000
    forwardList = [
        [1,3000],
        [2,5000],
        [3,7000],
        [4,10000]
    ]
    returnList = [
        [1,2000],
        [2,3000],
        [3,4000],
        [4,5000]
    ]
    aircraftOptimum(maximumOperatingTravelDistance,
                    forwardList,
                    returnList)
