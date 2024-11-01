def build_heap(A,n):
    idx=n//2-1
    for i in range(idx,-1,-1):
        bubble_up(A,n,i)

def bubble_up(A,n,i):
    largest=i
    l_child=2*i+1
    r_child=2*i+2
    if l_child<n and A[l_child]>A[largest]:
        largest=l_child
    if r_child<n and A[r_child]>A[largest]:
        largest=r_child
    if largest!=i:
        temp=A[i]
        A[i]=A[largest]
        A[largest]=temp
        bubble_up(A,n,largest)


n=84174
input_str=""
A=list(map(int, input_str.split()))
build_heap(A,n)
result=A
with open("max_heap_tree.txt", "w") as f:
    f.write(' '.join(map(str, result)))