def iprb(k,m,n):
    tot_pop=k+m+n
    #probabilitiy of having at least one dominant allele when crossing the two genotypes
    prob_AA_AA=1
    prob_AA_Aa=1
    prob_AA_aa=1
    prob_Aa_Aa=0.75
    prob_Aa_aa=0.5
    
    AA_AA=(k/tot_pop)*((k-1)/(tot_pop-1))*prob_AA_AA
    AA_Aa=2*(k/tot_pop)*(m/(tot_pop-1))*prob_AA_Aa
    AA_aa=2*(k/tot_pop)*(n/(tot_pop-1))*prob_AA_aa
    Aa_Aa=(m/tot_pop)*((m-1)/(tot_pop-1))*prob_Aa_Aa
    Aa_aa=2*(m/tot_pop)*(n/(tot_pop-1))*prob_Aa_aa

    final=AA_AA+AA_Aa+AA_aa+Aa_Aa+Aa_aa

    print(final)

k=26
m=26
n=20
iprb(k,m,n)