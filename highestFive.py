# # # # -*- coding: utf-8 -*-
"""
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
每人至少有5份成绩，要取最高的5份的average
"""

# Solution 1
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

# Solution 2
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def getAvg(self, scores):
        return sum(scores) / 5.0

    def highFive(self, results):

        # process raw data
        record = {}
        for r in results:
            # student = r.id
            # score = r.score
            student = r[0]
            score = r[1]
            if student not in record:
                record[student] = []
            record[student].append(score)

        # if student has more than 5 scores, get top 5
        ans = {}
        for stu in record:
            if len(record[stu]) >= 5:
                record[stu] = sorted(record[stu], reverse = True)[:5]
                avg = self.getAvg(record[stu])
                ans.update({stu: avg})

        return ans

if __name__ == '__main__':
    array = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61],[1,100]]
    highestFive(array)

    s = Solution()
    print(s.highFive(array))