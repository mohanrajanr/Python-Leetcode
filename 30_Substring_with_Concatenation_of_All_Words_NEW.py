class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if s is None or words is None:
            return []

        length = len(words[0])
        num_of_word = len(words)
        total_length = length * num_of_word
        words_dict = self.buildWordDict(words)

        result = []

        for start in range(0,length):
            left = start
            right = start
            curr_dict = {}
            # right+length should always not exceed total length of s
            while right + length <= len(s):
                # get the current word
                word = s[right:right+length]
                # move right to the next word
                right += length
                # if the current word is valid in words_dict
                if word in words_dict:
                    # update the curr_dict so it can be compared with words_dict
                    curr_dict[word] = curr_dict[word] + 1 if word in curr_dict else 1
                    # below condition happens where there are more words added to curr_dict; thus we should move the left
                    while curr_dict[word] > words_dict[word]:
                        # left needs to move to the right by length position, so the next evaluation can start
                        curr_dict[s[left:left+length]] -= 1
                        left += length
                    if right - left == total_length:
                        result.append(left)
                        #left += length -- is this needed? No

                else:
                    curr_dict.clear()
                    left = right

        return result


    def buildWordDict(self, words):
        words_dict = {}
        for word in words:
            if word in words_dict.keys():
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        return words_dict

if __name__ == '__main__':
    s = Solution()
    #words = ['foo','bar','car']
    #words = "ab"

    str = "abarfoobara"
    words = ["foo", "bar"]
    indexes = s.findSubstring(str,words)
    print indexes