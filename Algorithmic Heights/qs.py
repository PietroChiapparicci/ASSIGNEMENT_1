import random

def qs(A,n):
    if n<=1:
        return A
    p=random.randint(0,n-1)
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
    return qs(left,len(left))+around_p+qs(right,len(right))

n=91792
input_str1=""
A=list(map(int, input_str1.split()))
sorted_A=qs(A,n)
with open("sorted_array.txt", "w") as f:
    f.write(' '.join(map(str, sorted_A)))