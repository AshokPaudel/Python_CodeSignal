##Find firstDuplicate 
#First Method

def firstDuplicate(a):
    a1=[]
    ind=-1
    ret=-1
        
    for  i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                if ind==-1:
                    ind=j
                    ret=a[j]
                if ind>j:
                    ind=j
                    ret=a[j]
    return ret
	

