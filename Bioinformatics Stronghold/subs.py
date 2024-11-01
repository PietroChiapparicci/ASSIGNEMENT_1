def subs(t,s):
    pos=[]
    for i in range (len(t)-len(s)+1):
        if t[i:i+len(s)]==s:
            pos.append(i)
    #adding 1 to each element of the list to make the number coincide with Rosalind's one
    for i in range(len(pos)):
        pos[i]+= 1
    return pos
t=""
s=""
result=subs(t,s)
result=' '.join(map(str,result))
print(result)