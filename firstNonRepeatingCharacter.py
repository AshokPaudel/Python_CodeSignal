def firstNotRepeatingCharacter(s):
    ret='_'
    #print('a' not in 'bc')
    i=2
    #cmp_str=s[0:i-1]+s[i+1:len(s)]
    #print(cmp_str)
    #print(s[0+1:len(s)])
    for i in range(len(s)):
        cmp_str=s[0:i-1]+s[i+1:len(s)]
        #print(cmp_str)
        if s[i] not in cmp_str:
            return s[i]
    return ret
    
	#This code will take some time, faster would be if you use index and rindex will be faster
	
	#faster code
	#for i in s:
    #   if s.index(i)==s.rindex(i):
    #       return i       
    #return ret
	
	#if s[i] not in s[i+1:] and s[i] not in chk:
     #       return s[i]
	
	#rindex(str): Python string method rindex() returns the last index where the substring str is found, or raises an exception 
	#if no such index exists, optionally restricting the search to string[beg:end]
	#The index() method finds the first occurrence of the specified value.
	
            