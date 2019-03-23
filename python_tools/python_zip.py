# # # # -*- coding: utf-8 -*-

"""
zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。利用*号操作符，可以将list unzip（解压），看下面的例子就明白了：

# >>> a = [1,2,3]
# >>> b = [4,5,6]
# >>> c = [4,5,6,7,8]
# >>> zipped = zip(a,b)
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(a,c)
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(*zipped)
# [(1, 2, 3), (4, 5, 6)]
"""
if __name__ == '__main__':
    quality = [10, 20, 5]
    wage = [70, 50, 30]
    temp = [(w, q) for w, q in zip(wage, quality)]
    print(temp)
    workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
    print(workers)
