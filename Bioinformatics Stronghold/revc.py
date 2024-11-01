def revc(s):
    src=""
    for i in range(len(s)-1,-1,-1):
        if s[i]=="A":
            src+="T"
        elif s[i]=="T":
            src+="A"
        elif s[i]=="G":
            src+="C"
        elif s[i]=="C":
            src+="G"
    print(src)

s=""
revc(s)
