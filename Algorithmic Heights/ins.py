def ins(a,n):
    idx=0
    for i in range(1,n): 
        key = a[i] 
        j=i-1 
        while j>=0 and key<a[j]: 
            a[j+1]=a[j] 
            j-=1 
            idx+=1
        a[j+1]=key
    print(idx)

n=932
input_str=""
a=list(map(int, input_str.split()))
ins(a,n)