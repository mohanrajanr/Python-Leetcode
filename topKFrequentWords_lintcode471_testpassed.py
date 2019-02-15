# # # # -*- coding: utf-8 -*-

def topKFrequentWords(words, k):
    # write your code here
    result = []
    temp = {}
    for w in words:
        if w not in temp:
            temp[w] = 0
        temp[w] += 1
    temp = sorted(temp.iteritems(), key=lambda x: x[0])
    temp = sorted(temp, key=lambda x: x[1], reverse=True)
    for i in range(k):
        result.append(temp[i][0])
    return result

words = [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]

k = 3

print topKFrequentWords(words, k)
