# A function that takes as its input a number (n) and converts it to a string, the contents of which depend on the numbers factors

# if the number has a factor of 3, output 'Pling' if the number has a factor of 5, output 'Plang' if the number has a factor of 7, output 'Plong' if the number does not have any of the above as a factor simply return the numbers digits

# Examples
# 28's factors are 1, 2, 4, 7, 14 and 28: this would be a simple 'Plong' 30's factors are 1, 2, 3, 5, 6, 10, 15, 30: this would be a 'PlingPlang' 34 has four factors: 1, 2, 17, and 34: this would be '34'







def RainDrops(n):
    
    res = []                #this list will contain the result to return

    if n % 3 == 0:
        res.append('Pling')             #If number n has factor of 3 then append "Pling" to the list
    if n % 5 == 0:
        res.append('Plang')             #If number n has factor of 5 then append "Plang" to the list
    if n % 7 == 0:
        res.append('Plong')             #If number n has factor of 7 then append "Plong" to the list

    if len(res) != 0:                   #Now checking if number n either has any one factor among 3,5,7 (the length of res will determine this)
        return "".join(res)             #Then convert all the values present in list as one string and return that result(here we are joining the all strings)
    else:
        return "".join(str(n))          #If number has none of factor among 3,5 and 7 then return that number as string


if __name__ == '__main__':
    #testcases to check
    print('105 = ' + RainDrops(105))
    print("30 = " + RainDrops(30))
    print("25 = " + RainDrops(25))
    print("28 = " + RainDrops(28))
    print("34 = " + RainDrops(34))
    print("280 = " + RainDrops(280))