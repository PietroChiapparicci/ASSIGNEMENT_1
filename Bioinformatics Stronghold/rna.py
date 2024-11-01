def rna(t):
    u=""
    for i in t:
        if i=="T":
            u+="U"
        else:
            u+=i
    print(u)

t=""
rna(t)
