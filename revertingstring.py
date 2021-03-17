# Reverting String in Python in O(n) Complexity
def revertingString(x):
    str = ""
    for word in x:
        str = word + str
    return str    

phrase = "Hi my name is Dimbu"
print(revertingString(phrase))


# Reverting a string in O(1) complexity
def revertingString(x):
    print(x[::-1])
  
phrase = "My name is Dimbu"
revertingString(phrase)