#this function will return the smallest integer, smaller than upperBound not present in s, if not found return the upperbound
#The highlight is you can use else in for loop as well. 
#Hint: for loops also have an else clause which executes when the loop completes normally, i.e. without encountering any breaks
def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found=upperBound

    return found
