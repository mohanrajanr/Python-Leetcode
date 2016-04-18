class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if s is None:
            return []

        words_permutation = self.permutate(words)
        indexes = []
        for word in words_permutation:
            index = s.find(word)
            if index != -1:
                indexes.append(index)
        return indexes
    """
    def permutate(self, words):
        #:type words: str
        #:rtype: List[str]

        if len(words) <= 1:
            return list(words)

        L = []
        for i in range(0,len(words)):
            p = self.permutate(words[:i]+words[i+1:])
            for str in p:
                L.append(words[i] + str)
        return L
    """
    def permutate(self, words):
        """
        :param words: List[str]
        :return: List[str]
        """
        if len(words) <= 1:
            return words

        L = []
        for i in range(0, len(words)):
            words_to_be_permutated = words[:i] + words[i+1:] # This happens to be the same as single word permutation!
            p = self.permutate(words_to_be_permutated)
            for str in p:
                L.append(words[i] + str)
        return L

if __name__ == '__main__':
    s = Solution()
    #words = ['foo','bar','car']
    #words = "ab"

    str = "barfoothefoobarman"
    words = ["foo", "bar"]
    indexes = s.findSubstring(str,words)
    print indexes