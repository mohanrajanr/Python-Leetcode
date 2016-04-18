class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {
                      1000:'M',
                      500:'D',
                      100:'C',
                      50:'L',
                      10:'X',
                      5:'V',
                      1:'I'
                      }

        carry = [1000, 100, 10, 1]

        result = ""
        for key in sorted(roman_dict.keys(),reverse=True):
            if num >= key:
                while num >= 0:
                    times = num / key
                    if 0 < times <= 3:
                        while times > 0:
                            num -= key
                            result += roman_dict[key]
                            times -= 1
                    elif times == 4:
                        num -= key * 4
                        if result[-1:] == roman_dict[last_visited_key]:
                            result = result[:-1]
                            #result += roman_dict[key] + roman_dict[last_visited_key]
                            prev_carry_key = carry[carry.index(key) - 1]
                            result += roman_dict[key] + roman_dict[prev_carry_key]
                        else:
                            result += roman_dict[key] + roman_dict[last_visited_key]
                    else:
                        break
            last_visited_key = key

        return result

if __name__ == '__main__':
    s = Solution()
    num = 1437
    print s.intToRoman(num)