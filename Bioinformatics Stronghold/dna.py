def dna(s):
    idxA=0
    idxC=0
    idxG=0
    idxT=0
    for i in s:
        if i=="A":
            idxA+=1
        elif i=="C":
            idxC+=1
        elif i=="G":
            idxG+=1
        else:
            idxT+=1
    print (idxA,idxC,idxG,idxT)

s=""
dna(s)