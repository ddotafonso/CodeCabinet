# Finding longest word in O(n)

phrase = "I am in love Italy and Australia"

def longestWord(x):
    longest = ""
    sentence = x.split(" ")
    for word in sentence:
        if len(word) > len(longest):
            longest = word
    return longest
        


print(longestWord(phrase))