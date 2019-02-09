# # # # -*- coding: utf-8 -*-
def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    if num == 1:
        return arr[0]
    elif num == 2:
        return gcd_two(arr[0],arr[1])
    else:
        new_gcd_lst = []
        for n in arr:
            if n != arr[0]:
                temp = gcd_two(n, arr[0])
                new_gcd_lst.append(temp)
        new_gcd_lst=list(set(new_gcd_lst))
        return generalizedGCD(len(new_gcd_lst), new_gcd_lst)

def gcd_two(num1, num2):
    smaller = num1 if num1 < num2 else num2
    result = 1
    for i in range(1, smaller+1):
        if num1 % i == 0 and num2 % i == 0:
            result = i
    return result



if __name__ == '__main__':
    # arr = [2,3,4,5,6]
    arr = [2,4,6,8,10]
    num = 5
    print(generalizedGCD(num,arr))