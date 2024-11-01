from Bio import SeqIO


def gc(dna):
    counterGC=0
    for i in dna:
        if i=="C" or i=="G":
            counterGC+= 1
    result=(counterGC*100)/len(dna)
    return result

def max_gc(dna_data):
    highest_gc_id=None
    highest_gc_content=0
    for dna_id, dna_seq in dna_data:
        gc_content=gc(dna_seq)
        if gc_content>highest_gc_content:
            highest_gc_content=gc_content
            highest_gc_id=dna_id

    print(highest_gc_id) 
    print(highest_gc_content)

def parse_fasta():
    dna_data=[]
    for record in SeqIO.parse("rosalind_gc.txt", "fasta"): #rosalind dataset has to be present in the same folder as this file
        ID= record.id
        sequence=str(record.seq)
        dna_data.append((ID,sequence))
    return dna_data


dna_data=parse_fasta()
max_gc(dna_data)