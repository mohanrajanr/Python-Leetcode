# Python3 program to count number of
# substrings with exactly k distinct
# characters in a given string

# Function to count number of substrings
# with exactly k unique characters
def countkDist(str1, k):
    # Initialize result
    res = 0
    # Consider all substrings beginning
    # with str[i]
    result = []
    for i in range(0, len(str1)):
        dist_count = 0

        # Initializing array with 0
        characters_table = {}

        # Consider all substrings between str[i..j]
        for j in range(i, len(str1)):

            # If this is a new character for this
            # substring, increment dist_count.
            if str1[j] not in characters_table:
                characters_table[str1[j]] = 0
                dist_count += 1

            # Increment count of current character
            characters_table[str1[j]] += 1

            # If distinct character count becomes k,
            # then increment result.
            if (dist_count == k):
                res += 1
                result.append(str1[i:j+1])
            if (dist_count > k):
                break

    return res, result


# Driver Code
if __name__ == "__main__":
    str1 = "pqpqs"
    k = 2
    print("Total substrings with exactly", k,
          "distinct characters : ")
    print(countkDist(str1, k))

# O(N^2)
# only k distinct characters, but length could be more than k
