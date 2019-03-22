# # # # -*- coding: utf-8 -*-
# http://kodango.com/understand-defaultdict-in-python
from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.graph = defaultdict(lambda: {})
        self.buildGraph(equations, values, self.graph)
        # print graph
        result = []
        for q in queries:
            visited = set()
            visited.add(q[0])
            # print(self.getDistance(q[0], q[1], visited))
            distance = self.getDistance(q[0], q[1], visited)
            if distance is not None:
                result.append(distance)
            else:
                result.append(-1.0)
        return result

    def getDistance(self, start, end, visited):
        if start not in self.graph or end not in self.graph:
            return None # Not return -1.0
        if start == end:
            return 1.0
        for key, value in self.graph[start].items():
            if key not in visited:
                visited.add(key)
                if end == key:
                    return value
                res = self.getDistance(key, end, visited)
                if res is not None:
                    return res * value
        return None

    def buildGraph(self, equations, values, graph):
        for index, item in enumerate(equations):
            value = values[index]
            graph[item[0]][item[1]] = value
            graph[item[1]][item[0]] = 1.0 / value



if __name__ == '__main__':
    s = Solution()
    hash = defaultdict(lambda : {})
    print(hash['a']) # by default, if the key doesn't exist, the value is {}
    hash['a'] = 1
    hash['b'] = 2
    print(hash) # defaultdict(<function <lambda> at 0x104ffb1e0>, {'a': 1, 'b': 2})

    hash['c']['d'] = 1
    hash['d']['c'] = 2
    print(hash) # defaultdict(<function <lambda> at 0x10ed281e0>, {'a': 1, 'b': 2, 'c': {'d': 1}, 'd': {'c': 2}})
    for key, value in hash.items():
        print (key, value)
    print (hash['c'])
    for key, value in hash['c'].items():
        print (key, value)