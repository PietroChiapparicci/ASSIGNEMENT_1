def par3(A):
    q=A.pop(0)
    left=[] 
    right=[]
    middle=[]

    for i in A:
        if i<q:
            left.append(i)
        elif i>q:
            right.append(i)
        else:
            middle.append(i)
    
    B=left+middle+[q]+right
    return B


n=87934
input_str1=""
A=list(map(int, input_str1.split()))
B=par3(A)
with open("3way_partitioned_list.txt", "w") as f:
    f.write(' '.join(map(str, B)))