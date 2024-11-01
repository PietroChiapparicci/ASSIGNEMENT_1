def hamm(s, t):
    hamm_diff=0
    idx1=0
    idx2=0
    while idx1<len(s) and idx2<len(t):
        if s[idx1]!=t[idx2]:
            hamm_diff+=1
        elif s[idx1]==t[idx2]:
            hamm_diff+=0
        idx1+=1
        idx2+=1
    print(hamm_diff)
s=""
t=""
hamm(s,t)
