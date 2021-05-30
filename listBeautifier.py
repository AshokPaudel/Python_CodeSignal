#We just ignore first and last element and take other item in res
#look at the power of while loop, we can have multiple conditions in while conditining
#Reference https://www.python.org/dev/peps/pep-3132/ 
#
def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        first, *res,last = res
    return res