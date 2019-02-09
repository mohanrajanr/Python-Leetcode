"""
Given a paragraph and a list of banned words, return the most frequent word that
is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.
Words in the paragraph are not case sensitive.  The answer is in lowercase.



Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
"""


def mostCommonWord(paragraph, banned):
    filtered_str = ""
    for c in paragraph:
        if c.isalpha() or c == ' ':
            filtered_str += c
        elif c in "!?',;.":
            filtered_str += ' '
    str_lst = filtered_str.lower().split()
    count = {}
    for pure_string in str_lst:
        if pure_string not in banned:
            if pure_string not in count:
                count[pure_string] = 0
            count[pure_string] += 1
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)
    if result and result[0]:
        return result[0][0]
    return ""

if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # paragraph = ""
    paragraph = "a, a, a, a, b,b,b,c, c"

    banned = ["hit"]
    print(mostCommonWord(paragraph, banned))