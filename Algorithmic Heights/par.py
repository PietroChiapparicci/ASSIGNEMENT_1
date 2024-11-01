def par(A):
    q=A.pop(0)
    left=[] 
    right=[]
    
    for i in A:
        if i<=q:
            left.append(i)
        else:
            right.append(i)
    
    B=left+[q]+right
    return B


n=86249
input_str1=""
A=list(map(int, input_str1.split()))
B=par(A)
with open("2way_partitioned_list.txt", "w") as f:
    f.write(' '.join(map(str, B)))