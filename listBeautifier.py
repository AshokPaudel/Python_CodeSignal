def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        first, *res,last = res
    return res
#We just ignore first and last element and take other item in res