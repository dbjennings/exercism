dna_to_rna = {"G":"C","C":"G","T":"A","A":"U"}

def to_rna(dna_strand):

    rna_strand = ""

    for nuc in dna_strand:
        rna_strand += dna_to_rna[nuc]
    
    return rna_strand