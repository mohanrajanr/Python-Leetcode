# # # # -*- coding: utf-8 -*-
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        self.l.append(val)
        length = len(self.l)
        self.d[val] = length-1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
        remove_position = self.d[val] # val: remove_position
        length = len(self.l)
        last_element = self.l[length-1] # last_element: length-1
        self.l[length-1], self.l[remove_position] = self.l[remove_position], self.l[length-1]
        self.l.pop()
        self.d[last_element] = remove_position
        del self.d[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.l) == 0:
            return 0
        import random
        length = len(self.l)
        random_index = random.randint(0, length-1)
        return self.l[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    randomSet = RandomizedSet()
    randomSet.insert(1)

    randomSet.remove(2)

    randomSet.insert(2)

    randomSet.getRandom()

    randomSet.remove(1)
    randomSet.insert(2)
    randomSet.getRandom()