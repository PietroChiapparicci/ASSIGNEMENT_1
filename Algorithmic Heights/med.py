import random
def med(n,A,k):
    p=random.randint(0,n-1) #the pivot is choosed at random because the task was to implement a "linear time randomized algorithm"
    pivot=A[p]
    left=[]
    around_p=[]
    right=[]
    for i in A:
        if i<pivot:
            left.append(i)
        elif i==pivot:
            around_p.append(i)
        else:
            right.append(i)
    if k<=len(left):
        return med(len(left),left,k)
    elif len(left)<k<=len(left)+len(around_p):
        return pivot
    else:
        return med(len(right),right,k-len(left)-len(around_p))

n=85560
input_str1=""
A=list(map(int, input_str1.split()))
k=30992
result=med(n,A,k)
print(result)
