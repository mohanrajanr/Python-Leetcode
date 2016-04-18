"""
#right add and left minus
#if smaller roman number is on the right of bigger roman number, it is add
#if bigger roman number is on the right of smaller roman number, it is minus
#only I, X, C can be subtracted
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_dict = {
              'M' : 1000,
              'D' : 500,
              'C' : 100,
              'L' : 50,
              'X' : 10,
              'V' : 5,
              'I' : 1,
              }

        roman_chars = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        result = 0
        # in s, check the current char and next char
        index = 0
        while index < len(s):
            # This is when index is at the end of s
            if index + 1 == len(s):
                result += roman_dict[ s[index] ]
                break

            if roman_chars.index(s[index]) >= roman_chars.index(s[index+1]):
                result += roman_dict[ s[index] ]
                index += 1
            else:
                result -= roman_dict[ s[index] ]
                result += roman_dict[ s[index+1] ]
                index += 2

        # (Example: IX)
        # if next char (X)'s greater than current char (I), -> where in roman_char X's index is greater than I's index,
            # then it should be X's corresponding value 10 to subtract I's value 1
        # else, it should be add
        return result

if __name__ == '__main__':
    s = Solution()
    str = "CMI"
    str = "CXCIX"
    str = "MCDXXXVII"
    print s.romanToInt(str)