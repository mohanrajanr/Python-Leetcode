# # # # -*- coding: utf-8 -*-
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0) # head stores least recent use
        self.tail = Node(0, 0) # tail stores most recent use
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        # add node to the tail
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        self.tail.prev = node
        node.next = self.tail

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # Check if key exist in dict
        # if yes, put it at the end of DLL, return value
        # if no, return -1
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # Create the Node
        # Put the Node at front of DLL , or update the value in DLL
        # If DLL is full at capacity, remove end
        # Update dict
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
        node = Node(key, value)
        self._add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.dict[node.key]

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# class DoubleLinkedList(object):
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.dict = dict()
#         self.head = Node(0, 0) # head stores least recent use
#         self.tail = Node(0, 0) # tail stores most recent use
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     def _remove(self, node):
#         prev = node.prev
#         next = node.next
#         prev.next = next
#         next.prev = prev
#
#     def _add(self, node):
#         # add node to the tail
#         prev = self.tail.prev
#         prev.next = node
#         node.prev = prev
#         self.tail.prev = node
#         node.next = self.tail

    # def addFrontNode(self, node):
    #     if self.head is None:
    #         node.prev = None
    #         node.next = None
    #         self.head = node
    #         self.tail = node
    #     else:
    #         node.next = self.head
    #         self.head.prev = node
    #         self.head = node
    #     self.size += 1
    #     if self.size > self.capacity:
    #         self.size -= 1
    #         self.removeEndNode()
    #
    # def removeEndNode(self):
    #     if self.tail:
    #         new_end = self.tail.prev
    #         self.tail.prev = None
    #         new_end.next = None
    #         self.tail = new_end


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)        # // returns 1
    cache.put(3, 3)     # // evicts key 2
    cache.get(2)        # // returns -1 (not found)
    cache.put(4, 4)     # // evicts key 1
    cache.get(1)        # // returns -1 (not found)
    cache.get(3)        # // returns 3
    cache.get(4)        # // returns 4
