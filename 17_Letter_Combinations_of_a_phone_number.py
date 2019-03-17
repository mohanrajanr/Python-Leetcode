# # # # -*- coding: utf-8 -*-
class Solution(object):
    def letterCombinations(self, digits):
        mapping = { "0":"",\
                    "1":"",\
                    "2":"abc",\
                    "3":"def",\
                    "4":"ghi",\
                    "5":"jkl",\
                    "6":"mno",\
                    "7":"pqrs",\
                    "8":"tuv",\
                    "9":"wxyz",
                    }
        digits = digits.replace("0","").replace("1","")

        if digits is None or digits == "":
            return []

        new_strs = [i for i in mapping[digits[0]] ]
        for i in range(1,len(digits)):
            # current digit : digits[i]
            chars = mapping[digits[i]]
            new_strs = self.getCharCombinations(new_strs,chars)
        return new_strs

    def getCharCombinations(self, strs, chars):
        if chars == "":
            return strs
        new_strs = []
        for char in chars:
            for each in strs:
                new_str = each + char
                new_strs.append(new_str)
        return new_strs

if __name__ == '__main__':
    s = Solution()
    digits = '234'
    print(s.letterCombinations(digits))
