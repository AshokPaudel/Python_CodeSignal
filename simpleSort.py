def simpleSort(arr):
#The highlight is how we can swap variables in python, without creating temporary variable
    n = len(arr)
    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j+1],arr[j] =arr[j], arr[j+1]
            j += 1
    return arr
    