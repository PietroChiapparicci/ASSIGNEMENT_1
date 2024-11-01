def mer(n,A,m,B):
    i=0
    z=0
    C=[]
    while i<n and z<m:
        if A[i]<B[z]:
            C.append(A[i])
            i+=1
        elif B[z]<A[i]:
            C.append(B[z])
            z+=1
        else:
            C.append(A[i])
            C.append(B[z])
            i+=1
            z+=1
    while i<n:
        C.append(A[i])
        i+=1

    while z<m:
        C.append(B[z])
        z+=1
    
    return C


n=4
input_str1=""
A = list(map(int, input_str1.split()))

m=3
input_str2=""
B= list(map(int, input_str2.split()))

C=mer(n,A,m,B)

with open("merged_list.txt", "w") as f:
    f.write(' '.join(map(str, C)))

