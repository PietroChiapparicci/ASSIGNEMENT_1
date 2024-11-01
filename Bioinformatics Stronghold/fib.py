def rabbit_pairs(n,k):
    if n==1:
        return 1
    elif n==2:
        return 1
    prev=1
    curr=1
    for month in range(3,n+1):
        next_gen=curr+k*prev
        prev=curr
        curr=next_gen
    return(curr)

n=31
k=5
print(rabbit_pairs(n, k))
